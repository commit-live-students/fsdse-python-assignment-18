def solution(dic1, dic2):
    for k,v in dic2.iteritems():
        dic1[k] = v
    return dic1
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
print solution(dic1,dic2)
