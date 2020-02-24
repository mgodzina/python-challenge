import zipfile
from io import BytesIO
import urllib.request
input = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
archive = zipfile.ZipFile(BytesIO(input.read()), 'r')


def get_number(nothing):
    input = archive.read(str(nothing)+'.txt')
    numbers = [int(s) for s in input.split() if s.isdigit()]
    if len(numbers) > 0:
        return numbers[0]
    else:
        return -1

next=1
nothing=90052
comments = ''
while(next>0):
    next = get_number(nothing)
    if next > 0:
        nothing = next
        print(nothing)
        comments = comments + archive.getinfo(str(nothing)+'.txt').comment.decode()

last = archive.read(str(nothing)+'.txt').decode()
print(last)
print(comments)

