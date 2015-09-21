#!/usr/bin/env python
"""
OB generator for GROND
=========================================================================

Generates .obd files with GROND OBs and can copy them to wgrond. These files
can then be loaded into bob and executed or imported into p2pp
Example: python OBgen.py -t GRB071031 -ob 30m6td 30m6td

Options:
=========================================================================
-target    Target Name (required, resolved by SIMBAD, searches in XRT GRB positions)
-ob        OBs (required, e.g., 30 30 for two 30 min OBs)
-ra        Right ascension (if target not known)
-dec       Declination (if target not known)
-cp        Copy to wgrond:/data/INSROOT/GROND/SYSTEM/COMMON/TEMPLATES/OBD/

Output:
=========================================================================
Creates one OB with several templates in a sub-directory of the current UTC day. 
The filename convention is "RA_DEC_TARGET_1stTemplate_TotalDuration.obd". There can 
be two 30min6td templates in one OB, and there is only one OB file per target.
=========================================================================
"""

import argparse
from OBclass import GRONDob

def obgen(args):
    gOB = GRONDob(args.target)
    gOB.setCoords(args.ra, args.dec)
    gOB.setObs(args.ob)
    gOB.setFileName()
    gOB.writeOB()
    if args.copy != None:
        gOB.uploadOB()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(usage=__doc__)
  parser.add_argument('-ob','--OB',dest="ob",nargs='+',type=list, default=[])
  parser.add_argument('-target','--target',dest="target",type=str,default='GRB')
  parser.add_argument('-ra','--RA',dest="ra",type=str,default=None)
  parser.add_argument('-dec','--DEC',dest="dec",type=str,default=None)
  parser.add_argument('-cp','--copy',dest="copy",type=str,default=None)
  args = parser.parse_args()
  if args.ob == [] or args.target == 'GRB':
    raise SystemExit("\n\tNeed -ob/-target arguments\n\tUse -h/--help for details!\n%s"%__doc__)
  else:
    obgen(args)