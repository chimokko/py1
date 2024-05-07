def find(obj, x):
    if type(obj) == list:
        for item in obj:
            res = find(item, x)
            if res != None:
                return res
    elif obj == x:
        return obj
    return None

print(find([1, 2, [3, 4, [5, [6, []]]]], 4))
print(find([1, 2, [3, 4, [5, [6, []]]]], 'spam'))