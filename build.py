def solution(dic1, dic2):
    dic = {}
    for d in [dic1,dic2]:
        dic.update(d)
    return dic

print solution({1: 10, 2: 20}, {3: 30, 4: 40})
