def solution(dic1, dic2):
    """Enter code here"""
    new_dic = dict(dic1.items() + dic2.items())
    return new_dic

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
print(solution(d1,d2))
