import requests, gzip, bs4

f = open('../image3.jpg', 'rb')

out = gzip.GzipFile('out.jpg.gz', 'wb')

headers = {
    'Cookie': 'cookieconsent_dismissed=yes',
    'Origin': 'http://howhot.io',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryD0dDO1qg6HbmABjT',
    'Accept': '*/*',
    'Referer': 'http://howhot.io/',
    'Connection': 'keep-alive'
}



r = requests.post('http://howhot.io/main.php', out)