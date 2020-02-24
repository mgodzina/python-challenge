import collections
input  = open('02_import', 'r').read() #file closing left for garbage collection
occurences = collections.Counter(input)

output = ''
for char in occurences:
    if occurences[char] < 5:
        output = output + char


print(occurences.most_common()[:-10-1:-1])
print(output)
print("http://www.pythonchallenge.com/pc/def/" + output +".html")
