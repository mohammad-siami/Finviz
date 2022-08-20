from typing import Collection
import requests
import json
import pymongo
from pymongo import MongoClient, InsertOne

url = 'https://finviz.com/api/quote.ashx?aftermarket=true&instrument=stock&patterns=true&premarket=true&rev'\
      '=1660985515927&ticker=SOGU&timeframe=m&type=new'
headers = {'authority': 'finviz.com',
           'accept': '*/*',
           'accept-language': 'en-US,en;q=0.9',
           'cookie': '_fssid=23bcb2e8-2de7-42ff-9d00-3612da92c73d; __qca=P0-1419467739-1659408547416;'
                     '_pbjs_userid_consent_data=3524755945110770; insiderTradingUrl=insidertrading.as'
                     'hx%3Ftc%3D7; __stripe_mid=1df09701-76eb-463d-ab99-7af842de3016a78096; affiliate'
                     'ID=128493348; customTable=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C65%2C66%2C67; euconse'
                     'nt-v2=CPdLngAPdLngAAKArAENCaCsAP_AAH_AACRQI6td_X__bW9j-_5_aft0eY1P9_r37uQzDhfNk'
                     '-8F3L_W_LwXx2E7NF36pq4KmR4Eu1LBIQNlHMHUDUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGF9Pn1tj'
                     'uYKY7_5_9_bx2D-t_9_-39T378Xf3_dp_2_-_vCfV599jfn9fV_789KP9_79v-_8__________3_4I7'
                     'AEmGrcQBdmWODNoGEUKIEYVhIVQKACCgGFogsAHBwU7KwCXWELABAKEIwIgQ4gowYBAAIJAEhEAEgRY'
                     'IBEARAIAAQAIgEIAGJgEFgBYGAQAAgGhYoBQACBIQZEBEcpgQFQJBQS2ViCUFehphAHWeAFBojYqABE'
                     'kgIpAQEhYOAYIkBLxZIGmKN8gBGCFAKJUAA.YAAAAAAAAAAA; _cmpRepromptHash=CPdLngAPdLng'
                     'AAKArAENCaCsAP_AAH_AACRQI6td_X__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwXx2E7NF3'
                     '6pq4KmR4Eu1LBIQNlHMHUDUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGF9Pn1tjuYKY7_5_9_bx2D-t_9'
                     '_-39T378Xf3_dp_2_-_vCfV599jfn9fV_789KP9_79v-_8__________3_4I7AEmGrcQBdmWODNoGEU'
                     'KIEYVhIVQKACCgGFogsAHBwU7KwCXWELABAKEIwIgQ4gowYBAAIJAEhEAEgRYIBEARAIAAQAIgEIAGJ'
                     'gEFgBYGAQAAgGhYoBQACBIQZEBEcpgQFQJBQS2ViCUFehphAHWeAFBojYqABEkgIpAQEhYOAYIkBLxZ'
                     'IGmKN8gBGCFAKJUAA.YAAAAAAAAAAA.1.QjY0v9UMqYSBhGAhdjRltA%3D%3D; cookie=99d6d5c8-'
                     '8eb1-4989-8732-20b6a63f14c8; __gads=ID=8068fc69b213741d:T=1660203108:S=ALNI_MZj'
                     'mIi4h4TXbZ4jWXhpjas4RZEtEg; _lr_env_src_ats=false; _cc_id=9a2ca4f2a4eeee913ba54'
                     'bf9fa4ba468; __gpi=UID=000007cc650bf673:T=1660203108:RT=1660377754:S=ALNI_MbNqP'
                     'w6MyUobRimzT9wPBU0h6zf2w; screenerUrl=screener.ashx%3Fv%3D111; cto_bundle=36C5G'
                     'F85YTZDZUQ0YmwwemJ2SWFMMlN2ZUJURnlVWlB0S2I0SnoxYlpSTW13dnJaZlNXRU11MUFwbSUyQkhu'
                     'QldwaDdveTV4VnZ0emtBU0FVR0lPR3lDdjhaNTJ6RHljT1NabEQ3Wk90U05EVHVPdkF2TU5RQ0trdXZ'
                     'VOGFSelhnbGFiSFolMkJBS3p3bmVmTFVjVzQ0V3I2TDB6Y3VRJTNEJTNE; cto_bidid=4Pku919sbU'
                     'JXWW00REw5SmpBQ3phbEwlMkZRR1NqdmVoRGpYdDZNdTJlZVpXaGVPVmIwQW1USEdBYnRCMCUyRm1Lb'
                     'XBSeGxZSWZCZkR2czFaUU9sMkJjWHBwQlglMkJob2N3cnJYdTRncXpVUlJObzRIZlN6ZyUzRA; .ASP'
                     'XAUTH=D14F8D5FA326E396C44BAF626D6D0EE2CF295C6BEBA1FDC0217B653DB2F265A5697CC1FCF'
                     'CDB749C9AA33904E8633EB0D69C65E99132CCB71F77FF9F662DCDFF60017A9D262E311AF8F85E50'
                     '6DECFF8C52B0A91A5C42402FD9766805121AC7E0BF37E5D42B987595828DC88F3EA712F072AF8ED'
                     'D8A0C2AF4A928FC7782A68CFB15172B94EC8E844EF6B61172793DDB508754DF20589A74DA83F04E'
                     '3923D733C0F6A3D560289559382B8C0D12F5DD8E47F38DB109FE34B57FC7C29D100F4CA9C5C146C'
                     'A1B08533ED718B4125780F3C4E31F9792D9011800C66C06F0B04878B9061F70AB1A; pv_date=Sa'
                     't Aug 20 2022 08:12:07 GMT+0430 (Iran Daylight Time); _gid=GA1.2.1920211113.166'
                     '0966928; fsbotchecked=true; pv_count=9; _ga=GA1.1.633984869.1659408547; _ga_ZT9'
                     'VQEWD4N=GS1.1.1660985502.26.1.1660985515.0.0.0',
           'referer': 'https://finviz.com/quote.ashx?b=1&t=SOGU&ty=c&p=m&tas=0',
           'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Linux"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
           }

# Retrieve data from url
response = requests.get(url, headers=headers)
response_js = response.json()
# Write data to file:
date = str(response_js['lastDate'])[0: 6]
path = '/media/python/New Volume/Automation/JadiJadi/Projects/Finviz/SGOU/Monthly/' + date
with open(path, 'w') as f:
    json.dump(response_js, f)
# Making connection to Mongo
client = MongoClient('localhost', 27017)
db = client.finviz
collection = db[response_js['ticker'] + '_' + date]
# Write data from file to MongoDB
bulk_dict = []
with open(path) as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        bulk_dict.append(InsertOne(myDict))
result = collection.bulk_write(bulk_dict)
client.close()








