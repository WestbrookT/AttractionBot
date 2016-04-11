import requests

i = open('me.jpg', 'rb')






r = requests.post('http://howhot.io/main.php', files={'browseFile':('me.jpg', open('me.jpg', 'rb'))})

print(r.content)


