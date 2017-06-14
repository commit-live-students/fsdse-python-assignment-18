def solution(dic1, dic2):
    """Enter code here"""
    newDic = {}
    newDic = dict(dic1.items() + dic2.items())
    return newDic

solution({1: 10, 2: 20},{3: 30, 4: 40})
