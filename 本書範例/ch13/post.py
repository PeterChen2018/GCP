from firebase import firebase
url = 'https://chiouapp01-dedce.firebaseio.com'
fb = firebase.FirebaseApplication(url, None)
fb.post('/test', "Python")
fb.post('/test', {"name":"David"})