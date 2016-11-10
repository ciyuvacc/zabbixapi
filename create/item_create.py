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
    "method": "item.create",
    "params": {
        "name": "Free disk space on $1",
        "key_": "vfs.fs.size[/home/joe/,free]",
        "hostid": "30074",
        "type": 0,
        "value_type": 3,
        "interfaceid": "30084",
        "applications": [
            "609",
            "610"
        ],
        "delay": 30
    },
    "auth": "941ee02491f77255f3e7548326208e7e",
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
