from PIL import Image,ImageDraw
import urllib.request

url = 'http://www.pythonchallenge.com/pc/return/good.html'
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
request_url = opener.open(url)


contents = request_url.read().decode('unicode-escape').replace('\\n', '').replace('\\r', '')
# split first:, second searches for list of numbers. remove new lines, split by ',', map strings to integers
first = map(int, contents.split('first:')[1].split('second:')[0].replace('\n', '').split(','))
second = map(int, contents.split('second:')[1].split('-->')[0].replace('\n', '').split(','))

result = Image.new('1', (500,500))
draw = ImageDraw.Draw(result)
draw.line(tuple(first), fill='white')
draw.line(tuple(second), fill='white')

result.show()
