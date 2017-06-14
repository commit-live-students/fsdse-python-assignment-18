def solution(dic1, dic2):
    z = dic1.copy()
    z.update(dic2)
    return z

dic1={1: 10, 2: 20}
dic2={3: 30, 4: 40}
print (solution(dic1,dic2))
