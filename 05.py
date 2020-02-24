import urllib.request
import pickle

input = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
uncoded = pickle.load(input)
print(uncoded)

for line in uncoded:
    print("".join([symbol * padding for symbol, padding in line]))
