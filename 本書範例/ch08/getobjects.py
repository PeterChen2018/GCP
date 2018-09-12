import facebook
token="EAACEdEose0cBAA2TXAUVh5cVoWP2lxg04k9ST3MZBd7UeOAC0KDS5xPNtZB4dlEQkUxNeiKfxZA4o4r7PSkrpUHByVai2ZC64eakYE301zakh7iGfKUkPr0YfsNwQLyiantM26pA0wVLrOuGBqufJVWVlD8aVuPYRCmvZBZAT6ZCAZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')

post_ids = ['798156653603892_1077005465719008','798156653603892_1020234718062750']
posts = graph.get_objects(ids=post_ids)
for post_id in post_ids:
    p=posts[post_id]
    print(p["id"])
    print(p["message"])
    print()