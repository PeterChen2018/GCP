import requests,json

url="https://graph.facebook.com/v2.8/me/posts?access_token=EAACEdEose0cBAA2TXAUVh5cVoWP2lxg04k9ST3MZBd7UeOAC0KDS5xPNtZB4dlEQkUxNeiKfxZA4o4r7PSkrpUHByVai2ZC64eakYE301zakh7iGfKUkPr0YfsNwQLyiantM26pA0wVLrOuGBqufJVWVlD8aVuPYRCmvZBZAT6ZCAZDZD"
data = json.loads(requests.get(url).text) # 讀取資料並轉成 json 

for d in data['data']: # 讀取 Key 名稱為 data 的定典資料 
    if 'message' in d: # 確認 message 存在
        print("message:{}".format(d['message']))
        print("created_time:{}".format(d['created_time']))
        print("id:{}".format(d['id']))
        print()