import urllib.request
import re

request_url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
contents = str(request_url.read()).replace('\\n', '').replace('\\r', '')
input = re.split("<!--|--!>",contents)[1]

output = ''
for i in range(len(input)-9):
    if input[i].islower() and input[i+1:i+4].isupper() and input[i+4].islower() and input[i+5:i+8].isupper() and input[i+8].islower():
        output = output + input[i+4]
        print(input[i], input[i + 1:i + 4], input[i + 4], input[i + 5:i + 8], input[i + 8])

print(output)
