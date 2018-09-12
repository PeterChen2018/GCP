import facebook,os,shutil,requests

token="EAACEdEose0cBAA2TXAUVh5cVoWP2lxg04k9ST3MZBd7UeOAC0KDS5xPNtZB4dlEQkUxNeiKfxZA4o4r7PSkrpUHByVai2ZC64eakYE301zakh7iGfKUkPr0YfsNwQLyiantM26pA0wVLrOuGBqufJVWVlD8aVuPYRCmvZBZAT6ZCAZDZD"

graph = facebook.GraphAPI(access_token=token,version='2.7')

pages = graph.get_connections(id='me', connection_name='photos?fields=images')
photos = pages['data']
#print(photos)

if not os.path.exists("fb-photos"):  # 建立 fb-photo 目錄
    os.mkdir("fb-photos")

for p in photos:
    imagelst = p['images']
#    print(imagelst)
    for img in imagelst:
       filename = img['source'].split('/')[-1].split('?')[0]
       print(filename)
       f = open('fb-photos/'+filename, 'wb') #儲存照片的路徑、檔名
       pic = requests.get(img['source'], stream=True) #開啟照片
       shutil.copyfileobj(pic.raw, f) # 複製照片
       f.close()