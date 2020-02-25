from PIL import Image
from io import BytesIO
import urllib.request

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
request_url = opener.open(url)

img = Image.open(BytesIO(request_url.read()))
imgnew = Image.new('RGB',(int(img.width), int(img.height)))

for o in range(int(img.height)):
    for i in range(int(img.width/2)):
        imgnew.putpixel((i,o),img.getpixel(((i*2)+1-(o%2),o)))
        
for o in range(int(img.height)):
    for i in range(int(img.width/2)):
        imgnew.putpixel((i+320,o),img.getpixel(((i*2)+(o%2),o)))

imgnew.show()
