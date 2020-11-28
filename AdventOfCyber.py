#!/usr/bin/python3
import requests
host="http://10.10.169.100:3000"
nextrote=""
flag=""
while(nextrote !="end"):
    response=requests.get(host+"/"+nextrote)
    parsed=response.json()
    nextrote=parsed['next']
    if(nextrote != "end"):
        flag+=parsed["value"]
print(flag)