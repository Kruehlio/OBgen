#!/usr/bin/env python
"""
OB generator for GROND
=========================================================================

Generates .obx files with GROND OBs and copies them to wgrond.
Example: python OBgen.py -t GRB071031 -ob 30 30

Options:
=========================================================================
-target    Target Name (required, resolved by SIMBAD, searches in XRT GRB positions)
-ob        OBs (required, e.g., 30 30 for two 30 min OBs)
-ra        Right ascension (if target not known)
-dec       Declination (if target not known)
-cp        Copy to wgrond directory to
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
  if not args.ob != [] and not args.target != 'GRB':
    print("\tPlease give the required -ob/-target argument")
    print("\tUse -h/--help for details!")
  else:
    obgen(args)
