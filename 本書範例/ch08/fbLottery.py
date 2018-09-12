import facebook,random
token="EAACEdEose0cBAA2TXAUVh5cVoWP2lxg04k9ST3MZBd7UeOAC0KDS5xPNtZB4dlEQkUxNeiKfxZA4o4r7PSkrpUHByVai2ZC64eakYE301zakh7iGfKUkPr0YfsNwQLyiantM26pA0wVLrOuGBqufJVWVlD8aVuPYRCmvZBZAT6ZCAZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')
object_id='10154480724754354'

# 按讚
likeslist=[]
post = graph.get_object(id=object_id + '?fields=likes.limit(1000)')
likes = post['likes']['data']
print('共有', len(likes), '人按讚:')
for like in likes:
    #print (like['name'],end="、")
    likeslist.append(like['name'])

#留言
commentslist=[]
post = graph.get_object(id=object_id + '?fields=comments.limit(1000)')
comments = post['comments']['data']
print('共有', len(comments), '留言：')
for comment in comments:
    #print (comment['from']['name'],end="、")
    commentslist.append(comment['from']['name'])    
    
#按讚加留言者
personlist=[]
for p in likeslist:
    if p in commentslist:
        personlist.append(p)
print("按讚加留言者:",len(personlist))  
      
#抽獎  
no = random.randint(0,len(personlist)-1)
print("恭喜 {}XX，得到 iPhone7 Plus 壹台!".format(personlist[no][0:1]))