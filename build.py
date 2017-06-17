def solution(dic1, dic2):
    return dict(dic1.items() + dic2.items())


print solution({1: 10, 2: 20}, {3: 30, 4: 40})
