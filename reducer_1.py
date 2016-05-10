#!/usr/bin/env python

import sys

#create containers
curr_key = None
weblog = []
maleware = []

# input comes from STDIN
for line in sys.stdin:
    try:
        #parse the mapper_1.py input
        key, value = line.strip().split('\t')

        #check which piece of information is contained within the line
        if 'weblog' in value:
            #add to the list of weblog dates
            value = value.replace('_weblog', '')
            weblog.append(value)
            is_weblog = True
            is_maleware = False
        else:
            #add to the list of maleware names
            value = value.replace('_malware', '')
            maleware.append(value)
            is_weblog = False
            is_maleware = True

        if curr_key == key:
            #we are still on the same key
            continue
        else:
            #if curr_key is not None then we know this is not first instance,
            #  so reset the lists
            if curr_key is not None:
                #output all combinations of maleware name and weblog date
                for m in maleware[:-1 if is_maleware else len(maleware)]:
                    for w in weblog[:-1 if is_weblog else len(weblog)]:
                        print '%s\t%s' % (m, w)

                weblog = weblog[-1:] if is_weblog else []
                maleware = maleware[-1:] if is_maleware else []

            #reset the current key
            curr_key = key
    except:
        pass

#output the last key
try:
    for m in maleware:
        for w in weblog:
            print '%s\t%s' % (m, w)
except:
    pass
