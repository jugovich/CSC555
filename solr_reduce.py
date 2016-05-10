#!/usr/bin/env python
import sys
import pysolr
import re

ix_data = []
solr = pysolr.Solr('http://54.148.223.47:8983/solr/collection1/', timeout=30)

curr_key = None
# input comes from STDIN
for line in sys.stdin:
    try:
        #parse the mapper_1.py input
        key, value = line.strip().split('\t')
        _id, _text = re.match('(.*?)\|(.*)', value).groups()
        _payload = {'id': _id, 'post_text': _text}
        ix_data.append(_payload)

        #commit 5000 records at a time
        if len(ix_data) == 5000:
            solr.add(ix_data)
            ix_data = []

    except:
        raise

#index any remaining records
if ix_data:
    solr.add(ix_data)





#!/usr/bin/env python
import sys

# input comes from STDIN
for line in sys.stdin:
    try:
        #parse the mapper_1.py input
        key, value = line.strip().split('\t')
        print value

    except:
        raise




#!/usr/bin/env python
import sys
import re

curr_key = None
# input comes from STDIN
for line in sys.stdin:
    try:
        #parse the mapper_1.py input
        key, value = line.strip().split('\t')
        _id, _text = re.match('(.*?)\|(.*)', value).groups()

        if curr_key != key:
            '/home/ec2-user/reddit_posts_thread_%s' %
        with closing(open('/home/ec2-user/reddit_posts_thread'))


        #commit 5000 records at a time
        if len(ix_data) == 5000:
            solr.add(ix_data)
            ix_data = []

    except:
        raise

#index any remaining records
if ix_data:
    solr.add(ix_data)