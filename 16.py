from PIL import Image
from io import BytesIO
import urllib.request

url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
request_url = opener.open(url)

img = Image.open(BytesIO(request_url.read()))
imgnew = Image.new(img.mode, (img.width,img.height))

def shift(x,y,img,imgnew):
    for i in range(img.width):
        if x + i >= img.width:
            x = x - img.width
        imgnew.putpixel((i,y),img.getpixel((x+i,y)))


print(img.getextrema())
for o in range(img.height):
    for i in range(img.width):
        if img.getpixel((i,o)) > 230:
            shift(i,o,img,imgnew)
            break

imgnew.show()
