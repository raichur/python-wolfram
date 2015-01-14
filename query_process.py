#!/usr/bin/python

import sys
import wolframalpha
import app_key

# API KEY
app_id = app_key.app_id
client = wolframalpha.Client(app_id)
query = ' '.join(sys.argv[1:])
res = client.query(query)

if len(res.pods) > 0:
 texts = ""
 pod = res.pods[1]
 if pod.text:
  texts = pod.text
 else:
  texts = "I have no answer for that."
 texts = texts.encode('ascii', 'ignore')
 print texts
else:
 print "Sorry, I am not sure."
