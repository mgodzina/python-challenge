import urllib.request
import bz2

request_url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html')
contents = request_url.read().decode('unicode-escape').replace('\\n', '').replace('\\r', '')
user = contents.split('un: ')[1].split('\'')[1]
passwd = contents.split('pw: ')[1].split('\'')[1]


print(bz2.decompress(user.encode("raw_unicode_escape")))
print(bz2.decompress(passwd.encode("raw_unicode_escape")))
