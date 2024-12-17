# def get_matches_results(k):
#     def f(a, b, score):
#         if a==k or b==k:
#             results.append(score)
#             return
#         f(a+1, b, score+[f"{a + 1}:{b}"])
#         f(a, b+1, score+[f"{a}:{b + 1}"])
    
#     results = []
#     f(0, 0, ["0:0"])
#     return results

print(get_matches_results(1))
print(get_matches_results(2))

def get_matches_results(k):
    results = []
    queue = [(["0:0"], 0, 0)]
    
    while queue:
        score, a, b = queue.pop(0)
        if a==k or b==k:
            results.append(score)
            continue
        queue.append((score+[f"{a+1}:{b}"], a+1, b))
        queue.append((score+[f"{a}:{b+1}"], a, b+1))
    
    return results

print(get_matches_results(1))
print(get_matches_results(2))