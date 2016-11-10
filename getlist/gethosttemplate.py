#!/usr/bin/env python
#coding=utf-8
import json
import urllib2
#url = "http://192.168.6.9/zabbix/api_jsonrpc.php"
url = "http://10.10.2.134/api_jsonrpc.php"
header = {"Content-Type":"application/json"}

####auth user and password

data = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": ""
        }
    },
    "auth": "78a49e314c8ae8a0c576cf23676d7446",
    "id": 1
}

)

#create request object

request = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])

#auth and get auth id
try:
    result = urllib2.urlopen(request)
except URLError as e:
    print "gethost failed"
else:
    response = json.loads(result.read())
    result.close()
    print "Number Of Hosts:",len(response['result'])
    for template in response['result']:
        print "HostTemplate ID:",template['templateid'],"HostTemplate Name:",template['host']
