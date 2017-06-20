def solution(dic1, dic2):
    dic1.update(dic2)
    return dic1

a ={1: 10, 2: 20}
b = {3: 30, 4: 40}
solution(a,b)
