from PIL import Image
from io import BytesIO
import urllib.request

input_file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
img = Image.open(BytesIO(input_file.read()))

x = 0
line = []
for x in range(0, img.width, 7):
    pixel = img.getpixel((x, img.height / 2))
    if pixel[0] == pixel[1] == pixel[2]:
        line.append(pixel[0])

print(line)

output = ''
for c in line:
    output = output + chr(c)
print(output)

new_list = output[output.find('['):].strip('][').split(', ')
output = ''
for c in new_list:
    output = output + chr(int(c))
print(output)
