import facebook

token="EAACEdEose0cBAG4KWXRYEsx3R5ODadEe3eIZB7iCcDpZA3FACnE72g4b841ml1RbgoHFYW817PbwKSIEVHivkHXISKfW6WZCATTutvv2dzi14Jvj8SExUNmsg5GexCZBD5TSQZCOMbxtRIT2AYu5RCIxBb1oo1qwuPKgQJW9EaAZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')

message = "測試使用 Python 程式在 fb 上貼文!"
attachment =  {
	'name': '中老年人快樂學拍照、攝影', 
	'link': 'http://www.e-happy.com.tw/indexbookshow.asp?bid=278',
	'caption': '新書介紹',
	'description': '智慧型手機或平板電腦擁有多功能且方便隨身攜帶的優勢，拍出來的相片、影片還可以透過軟體直接編修美化與分享更是方便。本書以熟齡者用智慧型手機或平板電腦拍攝的角度出發，簡單易懂的說明與詳細的步驟講解，讓人人都能輕鬆用手機拍下身邊的風景，並與家人、朋友分享生活每一刻的心情。',
	'picture': 'http://www.e-happy.com.tw/images/bookimg/10-056-S.jpg'
}

graph.put_wall_post(message=message, attachment=attachment)
print("貼文成功!")