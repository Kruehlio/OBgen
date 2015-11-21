USER = 'grondmgr'
HOST = 'wgrond.ls.eso.org'
REMDIR = '/data/INSROOT/GROND/SYSTEM/COMMON/TEMPLATES/OBD/'

header = (
('PAF.HDR.START', '\t\t;', '\t# Marks start of header')   ,        
('PAF.TYPE', '\t\t"OB Description";', '\t# Type of parfile'),
('PAF.ID', '\t\t\t"";', '\t# Unused'),
('PAF.NAME', '\t\t"";', '\t# Unused'),
('PAF.DESC', '\t\t"";', '\t# Unused'),
('PAF.CRTE.NAME', '\t\t"BOB";', '\t# Broker for OBs'),
('PAF.CRTE.DAYTIM', '\t\t"2015-01-20T08:19:00";','\t# Date+time of creation'),
('PAF.LCHG.NAME', '\t\t"";','\t#  Unused'),
('PAF.LCHG.DAYTIM', '\t\t"2015-01-20T08:19:00";', '\t# Date+time of last change'),
('PAF.CHCK.NAME', '\t\t"";','\t# Unused'),
('PAF.CHCK.DAYTIM', '\t\t"";','\t# Unused'),
('PAF.CHCK.CHECKSUM', '\t"";','\t# Unused'),
('PAF.HDR.END', '\t\t;'  ,'\t# Marks end of header'),
) 

describtion = (
('OBS.ID', '\t"-1"'),
('OBS.DID', '\t"ESO-VLT-DIC.OBS-1.11"'),
('OBS.GRP', '\t"0"'),
('OBS.NAME', '\t\t""'),
('OBS.PI-COI.ID', '"0"'),
('OBS.PI-COI.NAME', ''),
('OBS.PROG.ID', ''),
('OBS.TARG.NAME', '"GRB"')
)

acquisition = (
('TPL.ID', '\t\t\t"GROND_img_acq"'),
('TPL.PRESEQ ', '\t\t"GROND_img_acq.seq"'),
('TPL.TYPE', '\t\t"acquisition"'),
('TPL.RESOURCES', '\t\t""'),
('TPL.NAME', '\t\t"Preset telescope"'),
('TPL.DID', '\t\t\t"ESO-VLT-DIC.TPL-1.9"'),
('TPL.INSTRUM', '\t\t"GROND"'),
('TPL.NEXP', '\t\t"1"'),
('TPL.EXECTIME', '\t\t"200"'),
('TPL.MODE', '\t\t""'),
('TPL.REFSUP', '\t\t"GROND_img_acq.ref"'),
('TPL.GUI', '\t\t\t""'),
('TPL.VERSION', '\t\t"$Revision: 1.4 $"'),
('TEL.AG.START', '\t\t"T"'),
('TEL.GS1.ALPHA', '\t\t"150000.00"'),
('TEL.GS1.DELTA', '\t\t"-270000.0"'),
('TEL.GS1.MAG', '\t\t"14"'),
('TEL.PRESET.NEW', '\t\t"T"'),
('TEL.TARG.ADDVELALPHA', '\t"0.0"'),
('TEL.TARG.ADDVELDELTA', '\t"0.0"'),
('TEL.TARG.ALPHA', '\t"150000.00"'),
('TEL.TARG.DELTA', '\t"-270000.0"'),
('TEL.TARG.EPOCH', '\t\t"2000"'),
('TEL.TARG.EQUINOX', '\t"2000"'),
('TEL.TARG.FOCOFFSET', '\t"0"'),
('TEL.TARG.NAME', '\t\t"GRB"'),
('TEL.TARG.PMA', '\t\t"0"'),
('TEL.TARG.PMD', '\t\t"0"'),
)


observation = (
('TPL.ID',  '\t\t\t"GROND_img_obs_exp"'),
('TPL.PRESEQ', '\t\t"GROND_img_obs_exp.seq"'),
('TPL.TYPE', '\t\t"science"'),
('TPL.RESOURCES', '\t\t""'),
('TPL.NAME', '\t\t"Science Imaging"'),
('TPL.DID', '\t\t\t"ESO-VLT-DIC.TPL-1.9"'),
('TPL.EXPNO', '\t\t"1"'),
('TPL.INSTRUM', '\t\t"GROND"'),
('TPL.NEXP', '\t\t\t"1"'),
('TPL.EXECTIME', '\t\t"computed"'),
('TPL.MODE', '\t\t"IMAGING"'),
('TPL.GUI',  '\t\t\t""'),
('TPL.REFSUP', '\t\t"GROND_img_obs_exp.ref"'),
('TPL.VERSION', '\t\t"$Revision: 1.4 $"'),
('DET1.DIT', '\t\t\t"10"'),
('DET1.IMODE',  '\t\t"Double"'),
('DET1.NDIT',  '\t\t\t"1"'),
('DET1.NINT',  '\t\t\t"1"'),
('DET2.NGR', '\t\t"1"'),
('DET2.NIZ', '\t\t"1"'),
('DET2.OMODE', '\t\t\t"slow"'),
('DET2.UITGR', '\t\t\t"35.4"'),
('DET2.UITIZ', '\t\t\t"35.4"'),
('INS.TARG.NMD', '\t\t\t"6"'),
('INS.TARG.NMP', '\t\t\t"6"'),
('TEL.COMBINED.OFFSET', '\t"T"'),
('TEL.PRESET.AUTO', '\t\t"F"'),
('TEL.TARG.FOCOFFSET', '\t"0"'),
('TEL.TARG.MAXSTAGE', '\t"9"'),
('TEL.TARG.NTD', '\t\t\t"4"'),
('TEL.TARG.NTP', '\t\t\t"4"'),
('TEL.TARG.OBSEQNUM', '\t"1"'),
('TEL.TARG.OBSRUNID', '\t"1"'),
('TEL.TARG.OBTYPEID', '\t\t"4m4td"'),
('TEL.TARG.TARGETID', '\t\t"GRB"'),
('TEL.TARG.TYPE', '\t\t"science"'),
)

#DIT, NDIT, NINT, OMODE, UIT, NMD, NMP, NTD, NTP
obtypes = {
'4m4td': [10, 1, 1, 'fast', 66., 6, 6, 4, 4, 380],
'4m4tds': [10, 1, 1, 'slow', 35., 6, 6, 4, 4, 380],
#'10m8td': [10, 1, 1, 'slow', 62, 8, 8, 8, 8, 980],
'10m8td': [10, 1, 1, 'fast', 92, 8, 8, 8, 8, 980],
#'8m4td': [10, 2, 1, 'slow', 115., 6, 6, 4, 4, 700],
'8m4td': [10, 2, 1, 'fast', 145., 6, 6, 4, 4, 700],  
#'20m4td': [10, 5, 1, 'slow', 330., 6, 6, 4, 4, 1600],
'20m4td': [10, 5, 1, 'fast', 360., 6, 6, 4, 4, 1600],
#'40m4td': [10, 10, 1, 'slow', 700., 6, 6, 4, 4, 3060],
'40m4td': [10, 10, 1, 'fast', 730., 6, 6, 4, 4, 3060],
#'6m6td': [10, 1, 1, 'fast', 66., 6, 6, 6, 6, 580],
'6m6td': [10, 1, 1, 'fast', 66., 6, 6, 6, 6, 580],
#'12m6td': [10, 2, 1, 'slow', 115., 6, 6, 6, 6, 1050],
'12m6td': [10, 2, 1, 'fast', 145., 6, 6, 6, 6, 1050],
#'18m6td': [10, 3, 1, 'slow', 180., 6, 6, 6, 6, 1440],
'18m6td': [10, 3, 1, 'fast', 210., 6, 6, 6, 6, 1440], 
#'24m6td': [10, 4, 1, 'slow', 250., 6, 6, 6, 6, 1860], 
'24m6td': [10, 4, 1, 'fast', 280., 6, 6, 6, 6, 1860],
#'30m6td': [10, 5, 1, 'slow', 330., 6, 6, 6, 6, 2340], 
'30m6td': [10, 5, 1, 'fast', 360., 6, 6, 6, 6, 2340],
#'60m6td': [10, 10, 1, 'slow', 700., 6, 6, 6, 6, 4560],
'60m6td': [10, 10, 1, 'fast', 730., 6, 6, 6, 6, 4560],
}
stdfields = {
'STD01_SDSS': ['00:40:00.0', '-21:53:42.0'],
'STD02_SDSS': ['01:40:00.0', '-18:03:00.0'],
'STD02E_SDSS': ['02:00:50.4', '-00:04:30.0'],
'STD02N_SDSS': ['02:00:12.0', '21:45:00.0'],
'STD03_SDSS': ['02:59:50.4', '-08:42:00.0'],
'STD03N_SDSS': ['03:00:48.0', '19:57:00.0'],
'STD04_SDSS': ['03:45:00.0', '-06:15:00.0'],
'STD05_SDSS': ['04:59:42.0', '-04:54:00.0'],
'STD06_SDSS': ['05:59:24.0', '05:39:00.0'],
'STD07_SDSS': ['06:59:33.6', '-17:27:00.0'],
'STD08_SDSS': ['07:59:52.8', '-10:18:00.0'],
'STD09_SDSS': ['09:00:36.0', '-02:18:00.0'],
'STD10_SDSS': ['10:00:00.0', '-02:42:00.0'],
'STD11_SDSS': ['10:50:36.0', '-21:36:00.0'],
'STD12_SDSS': ['11:27:00.0', '-03:10:00.0'],
'STD13_SDSS': ['12:42:00.0', '-22:30:00.0'],
'STD14_SDSS': ['14:21:36.0', '-22:33:00.0'],
'STD15_SDSS': ['14:56:48.0', '-02:48:00.0'],
'STD16_SDSS': ['15:52:00.0', '-01:30:00.0'],
'STD17_SDSS': ['17:00:24.0', '-11:18:00.0'],
'STD18_SDSS': ['17:34:16.8', '08:49:12.0'],
'STD19_SDSS': ['18:40:24.0', '20:19:12.0'],
'STD20_SDSS': ['20:00:36.0', '-11:09:36.0'],
'STD21_SDSS': ['21:33:40.0', '-00:23:00.0'],
'STD23_SDSS': ['23:00:33.0', '-10:09:00.0'],
}