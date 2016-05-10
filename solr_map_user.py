#!/usr/bin/env python

import sys

#read the input files
for line in sys.stdin:
    #use try/expect block to make sure a improperly formatted row does not blow our program up
    try:
        # remove leading and trailing whitespace
        # assume that the files are both comma delimited and only contain the columns described in assignment 4 part 1
        line = line.strip().split(",")

        _id, _text,  _user = line[0], line[5], line[20]
        #aggregate to the user level to create user indexes
        print '%s\t%s|%s' % (_user, _id, _text)

    except:
        #ignore errors
        pass