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
    "jsonrpc":"2.0",
    "method":"user.login",
    "params":{
    "user":"Admin",
    "password":"admin_1234"
},
"id":1
}
)

data69 = json.dumps(
{
    "jsonrpc":"2.0",
    "method":"user.login",
    "params":{
    "user":"YZ",
    "password":"wk99114"
},
"id":1
}
)

#create request object

request = urllib2.Request(url,data)
#request = urllib2.Request(url,data69)
for key in header:
    request.add_header(key,header[key])

#auth and get auth id
try:
    result = urllib2.urlopen(request)
except URLError as e:
    print "auth failed"
else:
    response = json.loads(result.read())
    result.close()
    print "Auth Succseeful,The Auth ID is:",response['result']
