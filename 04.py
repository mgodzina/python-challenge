import urllib.request
import re

def get_number(nothing):
    request_url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nothing))
    contents = str(request_url.read()).replace('\'', '').replace('\\r', '')
    numbers = [int(s) for s in contents.split() if s.isdigit()]
    if len(numbers) > 0:
        return numbers[0]
    else:
        return -1

next=1
nothing=12345
while(next>0):
    next = get_number(nothing)
    if next > 0:
        nothing = next
        if nothing == 16044: nothing = nothing / 2
        print(nothing)

request_url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nothing))
contents = str(request_url.read().decode())
print(contents)
print("http://www.pythonchallenge.com/pc/def/" + contents)
