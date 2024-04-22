import itertools
letters = "ivan"
res = itertools.product(letters, repeat=5)
q=0
for i in res:
    if "i" in i:
        q+=1
print(q)