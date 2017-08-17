def solution(dic1, dic2):
    d3 = {}
    d3 = dic1.copy()
    d3.update(dic2)
    return d3

print solution({1: 10, 2: 20},{3: 30, 4: 40})
