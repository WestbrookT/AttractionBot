import requests, gzip, bs4

f = open('../image3.jpg', 'rb')

out = gzip.GzipFile('out.jpg.gz', 'wb')

r = requests.post('http://howhot.io/main.php', out)