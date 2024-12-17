import sys
# def xi(k):
#     x = 1
#     for i in range(k):
#         x = (x+1)/(x+2)
#     return x
# print(xi(1))
# print(xi(2))
# print(xi(2228))

sys.setrecursionlimit(10000)
def xi(k):
    x0 = 1
    def eq(x,i):
        if i==k:
            return x
        x = (x+1)/(x+2)
        return eq(x,i+1)
    return eq(x0,0)
print(xi(1))
print(xi(2))
print(xi(2228))