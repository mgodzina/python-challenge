import sys
sys.setrecursionlimit(10**4)
start_number = '1'

def occure(number):
    recur=''
    result = 1
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            result += 1
        else:
            recur = occure(number[i+1:])
            break
    return str(result)+number[0]+recur

def an(start_number,n):

    a = [start_number]
    last = start_number
    for i in range(n-1):
        last = occure(str(last))
        a.append(int(last))
    return a

print(len(str(an(1,31)[30])))
