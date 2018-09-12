import facebook

token="EAACEdEose0cBAA2TXAUVh5cVoWP2lxg04k9ST3MZBd7UeOAC0KDS5xPNtZB4dlEQkUxNeiKfxZA4o4r7PSkrpUHByVai2ZC64eakYE301zakh7iGfKUkPr0YfsNwQLyiantM26pA0wVLrOuGBqufJVWVlD8aVuPYRCmvZBZAT6ZCAZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')

pages = graph.get_connections(id='me', connection_name='posts')

posts = pages['data']
#print(posts)

for p in posts:
    if 'message' in p:
        print('訊息：{}'.format(p['message']))
        print('貼文日期：{}'.format(p['created_time']))
        print()