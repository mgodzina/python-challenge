input  = open('03_import', 'r').read().replace('\n', '').replace('\r', '') #file closing left for garbage collection

output = ''
for i in range(len(input)-9):
    if input[i].islower() and input[i+1:i+4].isupper() and input[i+4].islower() and input[i+5:i+8].isupper() and input[i+8].islower():
        output = output + input[i+4]
        print(input[i], input[i + 1:i + 4], input[i + 4], input[i + 5:i + 8], input[i + 8])

print(output)
