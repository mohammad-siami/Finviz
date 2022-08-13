
import requests
import json 

url = 'https://finviz.com/api/quote.ashx?aftermarket=true&instrument=stock&patterns=true&premarket=true&rev=1660365755979&ticker=SOGU&timeframe=d&type=new'
headers = {'authority': 'finviz.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie':'_fssid=23bcb2e8-2de7-42ff-9d00-3612da92c73d; __qca=P0-1419467739-1659408547416; _pbjs_userid_consent_data=3524755945110770; insiderTradingUrl=insidertrading.ashx%3Ftc%3D7; .ASPXAUTH=4C94515915C6B16A712405159FE17DD153C40CBE9AE0CAB1CC1F84C9814053690BF15B3704670C0EF0F6E30234D5488877A2339D14C9B859AA783DF7D726D7F3D24EBD5B09DF17FC3EE5406234E563F775CFF6D5D2E4AD20E8E2E676FE2653A26FE86D1EA1D4FBD0989C26404A739EF00C72C9EBB9B4509A672B67C1A294A3E5B86D5ABFEDE35ABFF5D2E442C5114E113B166B9686D10FD082560DCD20CA882A682D3228AAF920B6B1267B8FDADDD94457C71CFB8669157D326B763227C48E9D0D0A7BCC72A1EE1CF5D6A4C64514335EC21B4A4C0AFF30E6D754B3F1353806E9135CCB1B; __stripe_mid=1df09701-76eb-463d-ab99-7af842de3016a78096; affiliateID=128493348; customTable=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C65%2C66%2C67; euconsent-v2=CPdLngAPdLngAAKArAENCaCsAP_AAH_AACRQI6td_X__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwXx2E7NF36pq4KmR4Eu1LBIQNlHMHUDUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGF9Pn1tjuYKY7_5_9_bx2D-t_9_-39T378Xf3_dp_2_-_vCfV599jfn9fV_789KP9_79v-_8__________3_4I7AEmGrcQBdmWODNoGEUKIEYVhIVQKACCgGFogsAHBwU7KwCXWELABAKEIwIgQ4gowYBAAIJAEhEAEgRYIBEARAIAAQAIgEIAGJgEFgBYGAQAAgGhYoBQACBIQZEBEcpgQFQJBQS2ViCUFehphAHWeAFBojYqABEkgIpAQEhYOAYIkBLxZIGmKN8gBGCFAKJUAA.YAAAAAAAAAAA; _cmpRepromptHash=CPdLngAPdLngAAKArAENCaCsAP_AAH_AACRQI6td_X__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwXx2E7NF36pq4KmR4Eu1LBIQNlHMHUDUmwaokVrzHsak2cpyNKJ7JEknMZO2dYGF9Pn1tjuYKY7_5_9_bx2D-t_9_-39T378Xf3_dp_2_-_vCfV599jfn9fV_789KP9_79v-_8__________3_4I7AEmGrcQBdmWODNoGEUKIEYVhIVQKACCgGFogsAHBwU7KwCXWELABAKEIwIgQ4gowYBAAIJAEhEAEgRYIBEARAIAAQAIgEIAGJgEFgBYGAQAAgGhYoBQACBIQZEBEcpgQFQJBQS2ViCUFehphAHWeAFBojYqABEkgIpAQEhYOAYIkBLxZIGmKN8gBGCFAKJUAA.YAAAAAAAAAAA.1.QjY0v9UMqYSBhGAhdjRltA%3D%3D; screenerUrl=screener.ashx%3Fv%3D111; cookie=99d6d5c8-8eb1-4989-8732-20b6a63f14c8; __gads=ID=8068fc69b213741d:T=1660203108:S=ALNI_MZjmIi4h4TXbZ4jWXhpjas4RZEtEg; __gpi=UID=000007cc650bf673:T=1660203108:RT=1660203108:S=ALNI_MbNqPw6MyUobRimzT9wPBU0h6zf2w; _lr_env_src_ats=false; _cc_id=9a2ca4f2a4eeee913ba54bf9fa4ba468; cto_bidid=UIjqFl9sbUJXWW00REw5SmpBQ3phbEwlMkZRR1NqdmVoRGpYdDZNdTJlZVpXaGVPVmIwQW1USEdBYnRCMCUyRm1LbXBSeGxZSWZCZkR2czFaUU9sMkJjWHBwQlglMkJoakFLR05rdk5GcFBReHZxZmVaZ2FuRSUzRA; cto_bundle=pMB3cF85YTZDZUQ0YmwwemJ2SWFMMlN2ZUJZSmowN096bHdBdDRTQ3U1YWdMVXhWRGJ2VFQlMkJHSkQwV3NhMjJqcVJaSXF4YVg4NEh2eEhzajdoM1Y0THc0c1I5dmpLZFlFcSUyQjdUTHoxRGF4M2RTdEdrUUo5JTJGRmhwamRZSWdaV1JNNlVSbVJzRCUyRjFZSVNkaHN5THVZZFJESCUyQnFBJTNEJTNE; pv_date=Sat Aug 13 2022 07:30:12 GMT+0430 (Iran Daylight Time); fsbotchecked=true; _gid=GA1.2.55865708.1660359613; pv_count=9; _ga=GA1.1.633984869.1659408547; _ga_ZT9VQEWD4N=GS1.1.1660363850.12.1.1660367004.0',
  'referer': 'https://finviz.com/quote.ashx?t=SOGU&ty=c&p=d&b=1',
  'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers).json()
#json_response = response.json()  
print(response)
print(response['volume'])
print(response['date'])
with open ('Finviz_json.json', 'w') as Finviz_js:
  json.dump(response, Finviz_js)    
  

  
  
  
  