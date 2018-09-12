import facebook
token="EAACEdEose0cBAOu451jVBbyb4ZCbX61pJwDAmqB3efayymZC4qtObbpGfuVZBivZAp2Kh9hCavT6JhdryJNkW9NvKtqNhD8SoZC8TPeuszZCClxurBXEpAq1qoTlbDfGLb85Ngy1XsMKYpnUM3gC0oHwvuZAfgzVdj3Lib1Q5QZCCwZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')

post = graph.get_object(id='798156653603892_1020234718062750?fields=message')
#print(post)
print('訊息：{}'.format(post['message']))
#

post = graph.get_object(id='798156653603892_1020234718062750?fields=likes')
likes = post['likes']['data']
print('共有', len(likes), '人按讚，：按讚者：')
for like in likes:
    print (like['name'],end="、")
print()

post = graph.get_object(id='798156653603892_1020234718062750?fields=comments')
comments = post['comments']['data']
print('共有', len(comments), '留言，：留言者：')
for comment in comments:
     print ("{}:{}".format(comment['from']['name'], comment['message']))
   
sharedposts = graph.get_object(id='798156653603892_1020234718062750?fields=sharedposts{from}')
sharedposts = sharedposts["sharedposts"]["data"]

print('共有', len(sharedposts), '人分享，：分享者：')
for sharedpost in sharedposts:
     print (sharedpost["from"]["name"])
