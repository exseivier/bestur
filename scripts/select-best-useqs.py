#!/usr/bin/env python

import dnaprocedures as dp
from sys import argv, exit

file_input = argv[1]
file_output = argv[2]
mfe = dp.loadMFE(file_input)
FHOUT = open(file_output, "w+")
for key, value in sorted(mfe.iteritems(), key=lambda (k,v): (v["nMFE"],k), reverse=True):
    FHOUT.write("%s\t%s\n" % (key, value))


