def solution(dic1, dic2):
    """Enter code here"""
    a = dict(dic1)
    a.update(dic2)
    return a


a, b = {1: 10, 2: 20}, {3: 30, 4: 40}

print solution(a,b)
