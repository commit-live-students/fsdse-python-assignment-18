def solution(dic1,dic2):
    dic = {}
    for d in (dic1, dic2):
        dic.update(d)
    return dic
