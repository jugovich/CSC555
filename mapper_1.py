#!/usr/bin/env python

import sys

#read the input files
for line in sys.stdin:
    #use try/expect block to make sure a improperly formatted row does not blow our program up
    try:
        # remove leading and trailing whitespace
        # assume that the files are both comma delimited and only contain the columns described in assignment 4 part 1
        line = line.strip().split(",")

        #use number of fields to determine file
        if len(line) == 6:
            #weblog file
            #output ip as key and date with _weblog appended as value
            print '%s\t%s_weblog' % (line[0], line[2])

        else:
            #melware file
            #output ip as key and malware name with _malware appended as value
            print '%s\t%s_malware' % (line[0], line[1])

    except:
        #ignore errors
        pass