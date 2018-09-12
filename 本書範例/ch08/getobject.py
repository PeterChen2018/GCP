import facebook
token="EAACEdEose0cBAA9ofhsgPfM4uv4TXZBk3rXDBMezZAjcTfbIgBbi2d8TsFPHzI5A4fJzSZAl806PvNUNU9lVagw1lwnKVu2O9oAc8DXRlFhkivUCw8ZAqPjZBEk4yz3kwZAvp35sGHHXN42EKMbGSJboxN9uz6lVdIhfrZChrHvOgZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')

post = graph.get_object(id='798156653603892_1077005465719008')
print(post["id"])
if 'message' in post:
    print(post["message"])
else:
    print("缺少 message 欄位")    