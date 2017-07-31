def solution(dic1, dic2):
    """Enter code here"""
    #return {**dic1,**dic2}
    ss=dic1.copy()
    ss.update(dic2)
    return ss
dic1={1:22,3:33}
dic2={2:3334,4:1212,3:32}
print(solution(dic1,dic2))
