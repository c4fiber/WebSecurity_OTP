import sys
from os import path
print ( path.dirname( path.abspath(__file__) ) )
sys.path.append(path.dirname( path.abspath(__file__) ) )

import generateOTP

def checkingOTP(argv):
    serial = argv[1]
    name = argv[2]
    tm = str(argv[3])

    generateOTP.getOTP(serial, name, False, tm)

checkingOTP(sys.argv)