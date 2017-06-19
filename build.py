def solution(dic1, dic2):
    """Enter code here"""
    result = {}
    result = dict(dic1.items() + dic2.items())
    return result

solution({1: 10, 2: 20},{3: 30, 4: 40})
