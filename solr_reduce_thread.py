#!/usr/bin/env python
import sys
import pysolr
import re
import requests

ix_data = []
curr_key = None

# input comes from STDIN
for line in sys.stdin:
    try:
        #parse the mapper_1.py input
        key, value = line.strip().split('\t')
        _id, _text = re.match('(.*?)\|(.*)', value).groups()
        _payload = {'id': _id, 'post_text': _text}
        ix_data.append(_payload)

        if curr_key != key:
            #dump remaining records for previous key
            if ix_data:
                solr.add(ix_data)

            #create the thread specific core
            requests.get('http://54.148.144.207:8983/solr/admin/cores?action=CREATE&name=thread_%s&instanceDir=%s&config=solrconfig.xml&schema=schema.xml&dataDir=data' % key)
            #connect to the solr collection
            solr = pysolr.Solr('http://54.148.144.207:8983/solr/thread_%s/' % key, timeout=30)

        #commit 5000 records at a time
        if len(ix_data) == 5000:
            solr.add(ix_data)
            ix_data = []

    except:
        raise

#output the last key
if ix_data:
    solr.add(ix_data)