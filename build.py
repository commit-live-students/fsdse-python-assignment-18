def solution(dic1, dic2):
    ndic = dict(dic1.items() + dic2.items())
    return ndic

print solution({1: 10, 2: 20}, {3: 30, 4: 40})
