a = 7*512**120 - 6*64**100 + 8**210 - 255
b = oct(a)[2:]
res = b.count('0')
print(res)