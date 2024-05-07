def find(obj, target):
    stack = [obj]
    
    while stack:
        current = stack.pop()
        
        if type(current) == list:
            stack.extend(current)
        elif current == target:
            return current
    
    return None

print(find([1, 2, [3, 4, [5, [6, []]]]], 4))
print(find([1, 2, [3, 4, [5, [6, []]]]], 'spam'))