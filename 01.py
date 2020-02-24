input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#original solution
def decode(str, n):
    output = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            if ( ord(char) + n ) > 122:
                output = output + chr(ord(char) + n - 26)
            else:
                output= output + chr(ord(char) + n)
        else:
            output= output + char
    return output

#solution includinh hint
def decode_by_hint(str):
    table_in = "abcdefghijklmnopqrstuvwxyz"
    table_out = "cdefghijklmnopqrstuvwxyzab"
    return str.translate(str.maketrans(table_in, table_out))

print(decode(input,2))
print(decode_by_hint(input))
