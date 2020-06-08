#!/usr/bin/python2
# desc: script to create encrypted passwords

import sys,crypt
if len(sys.argv) == 1 : sys.exit("you must provide a password as an argument")
print(crypt.crypt(sys.argv[1], crypt.mksalt(crypt.METHOD_SHA512)))

