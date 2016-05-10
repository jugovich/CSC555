#!/usr/bin/env python
import sys

#create containers
curr_key = None
count = 0
# input comes from STDIN
for line in sys.stdin:
    try:
        #parse the mapper_1.py input
        key, value = line.strip().split('\t')

        if curr_key != key:
            #if curr_key is not None then we know this is not first instance,
            #  so reset the lists
            if curr_key:
                print '%s\t%s' % (curr_key, count)
                #reset the count
                count = 0

            #set the current key
            curr_key = key

        #increment count
        count += 1

    except:
        pass

#output the last key
if curr_key == key:
    print '%s\t%s' % (curr_key, count)