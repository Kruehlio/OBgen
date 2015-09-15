import OBparams
import urllib
import sys
import datetime
import os
import re

XRTURL = 'http://www.swift.ac.uk/xrt_positions/index.php?basic=none&txt=1'
SESAMEURL = "http://cdsweb.u-strasbg.fr/cgi-bin/nph-sesame/-oI?"
SwiftURL = "http://swift.gsfc.nasa.gov/archive/grb_table/table.php?obs=Swift&year=All+Years&restrict=none&grb_time=1&grb_trigger=1"

class GRONDob:
    def __init__(self, target):
        if target.strip() != target:
            print 'ERROR: No blanks in targetname allowed'
            sys.exit()
        self.target = target
        self.header = OBparams.header
        self.acq = OBparams.acquisition
        self.OBs = []        
        self.obsDate = str(datetime.date.today())
        self.getTrig()


    def getTrig(self):
        if re.match("\d\d\d\d\d\d", self.target) or re.match("\d\d\d\d\d\d\D", self.target):
            self.target = 'GRB%s' %self.target
        self.targetid = self.target
        if re.match('GRB\d\d\d\d\d\d', self.target):
            response = urllib.urlopen(SwiftURL)
            html = response.read()
            response.close()
            grbpos = html.find(self.target[3:])
            if grbpos != -1:
                trignum =  re.findall(r'\d\d\d\d\d\d', html[grbpos:grbpos+100])
                if len(trignum) == 3:
                    print '\tSwift trigger number found: %s' %trignum[-1]
                    self.targetid = 'SWIFT-%s' %trignum[-1]

    def formatCoords(self, ra, dec):
        def addzero(val, n):
            if float(val) < 10:
                if n == 1: return '0%.0f' %val
                if n == 2: return '0%.2f' %val
            else:
                if n == 1: return '%.0f' %val
                if n == 2: return '%.2f' %val
        
        if not re.match("\d\d\d\d\d\d\.", ra):
          try:
            ra, dec = float(ra), float(dec)
            if ra < 0 or ra > 360 or dec < -90 or dec > 90:
                print '\tERROR: Malformed coordinated'
                print '\tERROR: No OB produced'
                sys.exit()
            hours = int(ra/15)
            minu = int((ra/15.-hours)*60)
            seco = float((((ra/15.-hours)*60)-minu)*60)
            degree = int(dec)
            minutes = int((dec-degree)*60)
            seconds = float((((dec-degree)*60)-minutes)*60)    
            retra = '%s%s%s' %(addzero(hours,1), addzero(minu,1), addzero(seco,2))
            if dec < 0:
                retdec = '-%s%s%s' %(addzero(-1*degree,1), addzero(-1*minutes,1), addzero(-1*seconds,2))
            else:
                retdec = '%s%s%s' %(addzero(degree,1), addzero(minutes,1), addzero(seconds,2))
          except ValueError:
            if len(ra.split(':')) == 3 and len(dec.split(':')) == 3:
              retra = ''.join(ra.split(':'))
              retdec = ''.join(dec.split(':')).strip('+')
            else:  
              print '\tERROR: Malformed coordinated'
              print '\tERROR: No OB produced'
              sys.exit()
        else:
            retdec, retra = dec, ra
        if float(retdec[:2]) > 40:
            print '\tWARNING: Coordinates > 40 deg'
        return retra, retdec

    def setCoords(self, ra=None, dec=None):
        print '\tSetting coordinates'
        if ra != None and dec != None:
            pass
        else:
          if self.target != 'GRB':
            # Resolve through Sesame
            print '\tResolving Target through Sesame'
            response = urllib.urlopen(SESAMEURL+'%s' %self.target)
            htmll = response.readlines()
            response.close()
            for html in htmll:
                entries = html.split()
                if len(entries) == 0:
                    print '\tTarget not found in SIMBAD'
                    break
                if entries[0] == '%J':
                    ra, dec = float(entries[1]), float(entries[2])
                    print '\tCoordinates found %s %s' %(ra, dec)
                    break
          if ra == None and dec == None:
            if self.target.startswith('STD'):
                if self.target in OBparams.stdfields.keys():
                    [ra, dec] = OBparams.stdfields[self.target]

          if ra == None and dec == None:
            print '\tSearching for Target in XRT GRB positions'
            response = urllib.urlopen(XRTURL)
            htmll = response.readlines()
            response.close()  
            for lines in htmll:
                grb = lines.split('|')
                grb = [a.replace(' ','') for a in grb]
                if len(grb) == 5:
                  if self.target in [grb[0], grb[0][3:]]:
                      ra, dec = grb[1], grb[2]
                      print '\tCoordinates found %s %s' %(ra, dec)

                                      
        if ra == None and dec == None:
            print 'ERROR - Target (-target) not known, Coordinates (-ra, -dec) not provided'
            print 'ERROR - No OBs created'
            sys.exit()
            
        self.ra, self.dec = self.formatCoords(ra, dec)
        print '\tCoordinates set %s %s' %(self.ra, self.dec)

    def setFileName(self):
        if float(self.dec)<0: decFile = self.dec[:3]
        else: decFile = '+%s' %self.dec[:2] 
        self.FileName = '%s_%s_%s_%s_%s.obx' %(self.ra[:2], decFile, self.target, self.OBs[0], self.obsDate )
#        print self.FileName
   
    def setObs(self, obs):
        obnames = [[[4,'4', '4m4td', '4min4td'], '4m4td'], 
                   [[8,'8', '8m4td', '8min4td',], '8m4td'],
                   [['4s', '4m4tds', '4min4tds'], '4m4tds'], 
                   [[10,'10', '10m8td', '10min10td'], '10m8td'],
                   [[20,'20', '20m4td', '20min4td'], '20m4td'], 
                   [[40,'40', '40m4td', '40min4td'], '40m4td'],
                   [[6,'6', '6m6td', '6min6td'], '6m6td'], 
                   [[12,'12', '12m6td', '12min6td'], '12m6td'],
                   [[18,'18', '18m6td', '18min6td'], '18m6td'], 
                   [[24,'24', '24m6td', '24min6td'], '24m6td'],
                   [[30,'30', '30m6td', '30min6td'], '30m6td'],
                   [[60,'60', '60m6td', '60min6td'], '60m6td']]
        for ob in obs:
            obok = 0
            ob = ''.join(ob)
            for obname in obnames:
                if ob in obname[0]:
                    self.OBs.append(obname[1])
                    obok = 1
            if obok == 0:
                print 'WARNING: DONT KNOW %s OB' %ob
    
    def writeOB(self, ):
        try:
            os.makedirs(self.obsDate)
        except OSError:
            pass
        self.OBfile = os.path.join(self.obsDate, self.FileName)
        
        f = open(self.OBfile, 'w')
        for head in OBparams.header:
            f.write('%s%s%s\n' %head)
        f.write('\n\n')

        for desc in OBparams.describtion:
            if desc[0] == 'OBS.NAME':
                f.write('%s\t\t"%s_%s"\n' %(desc[0], self.target, self.obsDate))
            else: f.write('%s\t\t%s\n' %desc)
        f.write('\n\n')

        for acq in OBparams.acquisition:
            if acq[0] in ['TEL.GS1.ALPHA', 'TEL.TARG.ALPHA']:
                f.write('%s\t\t"%s"\n' %(acq[0], self.ra))
            elif acq[0] in ['TEL.TARG.DELTA', 'TEL.GS1.DELTA']:
                f.write('%s\t\t"%s"\n' %(acq[0], self.dec))
            elif acq[0] == 'TEL.TARG.NAME':
                f.write('%s\t\t"%s"\n' %(acq[0], self.target))
            else: f.write('%s%s\n' %(acq[0], acq[1]))
        f.write('\n\n')

        i = 1
        for OB in self.OBs:
          obc = OBparams.obtypes[OB]
          for obs in OBparams.observation:
            if obs[0] == 'TPL.NEXP':
                f.write('%s\t\t"%s"\n' %(obs[0], obc[7]*(1+obc[6]*obc[2])))                
            elif obs[0] in ['DET1.DIT']: f.write('%s\t\t"%s"\n' %(obs[0], obc[0]))
            elif obs[0] in ['DET1.NDIT']: f.write('%s\t\t"%s"\n' %(obs[0], obc[1]))
            elif obs[0] in ['DET1.NINT']: f.write('%s\t\t"%s"\n' %(obs[0], obc[2]))
            elif obs[0] in ['DET2.OMODE']: f.write('%s\t\t"%s"\n' %(obs[0], obc[3]))
            elif obs[0] in ['DET2.UITGR', 'DET2.UITIZ']: 
                f.write('%s\t\t"%s"\n' %(obs[0], obc[4]))
            elif obs[0] in ['INS.TARG.NMD']: f.write('%s\t\t"%s"\n' %(obs[0], obc[5]))
            elif obs[0] in ['INS.TARG.NMP']: f.write('%s\t\t"%s"\n' %(obs[0], obc[6]))
            elif obs[0] in ['TEL.TARG.NTD']: f.write('%s\t\t"%s"\n' %(obs[0], obc[7]))
            elif obs[0] in ['TEL.TARG.NTP']: f.write('%s\t\t"%s"\n' %(obs[0], obc[8]))
            elif obs[0] == 'TEL.TARG.OBTYPEID':
                f.write('%s\t"%s"\n' %(obs[0], OB))
            elif obs[0] == 'TEL.TARG.OBSEQNUM':
                f.write('%s\t"%s"\n' %(obs[0], i))
                i+=1
            elif obs[0] == 'TEL.TARG.TARGETID':
                f.write('%s\t"%s"\n' %(obs[0], self.targetid))
            else: f.write('%s%s\n' %(obs[0], obs[1]))
          f.write('\n\n')            
        f.close()
        
    def uploadOB(self):
        #os.system('scp -r %s %s@%s:' %(self.obsDate, OBparams.USER, OBparams.HOST,
#                                       OBPARAMs.REMDIR))
        print ('scp -r %s %s@%s:%s' %(self.obsDate, OBparams.USER, OBparams.HOST,
                                       OBparams.REMDIR))
    def sendOB(self,):
        pass          
            