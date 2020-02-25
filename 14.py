from PIL import Image
from io import BytesIO
import urllib.request

url = 'http://www.pythonchallenge.com/pc/return/wire.png'
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
request_url = opener.open(url)

img = Image.open(BytesIO(request_url.read()))
imgnew = Image.new('RGB', (100,100))

d = 0
loop = 0

while d < img.width:
    for i in range(100)[0+loop:100-loop]:
        imgnew.putpixel((i,loop),img.getpixel((d,0)))
        d += 1
    for i in range(100)[0+loop + 1:100-loop]:
        imgnew.putpixel((99-loop, i), img.getpixel((d, 0)))
        d += 1
    for i in range(100)[0+loop+1:100-loop]:
        imgnew.putpixel((99-i,99-loop),img.getpixel((d,0)))
        d += 1
    for i in range(100)[0+1+loop:100-1-loop]:
        imgnew.putpixel((0+loop,99-i),img.getpixel((d,0)))
        d += 1
    loop += 1

imgnew.show()
