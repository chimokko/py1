k=0
num=0
for i in range(84052,84131):
    q=0
    for j in range(1,i+1):
        if i%j==0:
            q+=1
    if q>k:
        k=q
        num=i
print(k,num)