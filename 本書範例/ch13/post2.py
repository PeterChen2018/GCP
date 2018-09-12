from firebase import firebase
url = 'https://chiouapp01-dedce.firebaseio.com'
fb = firebase.FirebaseApplication(url, None)
dict1 = fb.post('/test', {"name":"David"})
print(dict1["name"])  # -KTMkuwiNbE18j9zpzko