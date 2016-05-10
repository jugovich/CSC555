#!/usr/bin/env python

import sys

#read the input files
for line in sys.stdin:
    #use try/expect block to make sure a improperly formatted row does not blow our program up
    try:
        # remove leading and trailing whitespace
        # assume that the files are both comma delimited and only contain the columns described in assignment 4 part 1
        line = line.strip().split(",")

        _id = line[0]
        _id, _text, _thread, _user = line[0], line[5] or 'N/A', line[10] or 'N/A', line[20] or 'N/A'

        #aggregate to the thread level to keep number of reduce jobs lower, and to also create thread specific indexes
        print '%s\t%s|%s' % (_thread.replace('\t', ''), _id.replace('\t', ''), _text.replace('\t', ''))

    except:
        #ignore errors
        raise
#
#
#
#
#!/usr/bin/env python
import sys

#read the input files
for line in sys.stdin:
    print (1, line[5] or 'N/A')




#!/usr/bin/env python
import sys
from hadoop.io import LongWritable
from hadoop.io import SequenceFile

writer = SequenceFile.createWriter('reddit_posts.seq' % _id, LongWritable, LongWritable)

#read the input files
for line in sys.stdin:

    #use try/expect block to make sure a improperly formatted row does not blow our program u
    # remove leading and trailing whitespace
    # assume that the files are both comma delimited and only contain the columns described in assignment 4 part 1
    line = line.strip().split(",")

    _id, _text, = line[0], line[5] or 'N/A'

    key = LongWritable()
    key.set(int(_id))

    value = LongWritable()
    value.set(_text)

    writer.append(key, value)

writer.close()


#!/usr/bin/env python
import sys

#read the input files
for line in sys.stdin:
    # remove leading and trailing whitespace
    # assume that the files are both comma delimited and only contain the columns described in assignment 4 part 1
    line = line.strip().split(",")

    _id, _text, _thread, _user = line[0], line[5] or 'N/A', line[10] or 'N/A', line[20] or 'N/A'

    #aggregate to the thread level to keep number of reduce jobs lower, and to also create thread specific indexes
    print '%s\t%s|%s' % (_thread.replace('\t', ''), _id.replace('\t', ''), _text.replace('\t', ''))


