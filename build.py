def solution(dic1, dic2):
    k1=dic1.keys()
    k2=dic2.keys()
    v1 = dic1.values()
    v2 = dic2.values()
    k1.extend(k2)
    v1.extend(v2)
    #print k1
    #print v1
    ts = zip(k1,v1)
    #print ts
    dz=dict(ts)
    return dz


solution({1: 10, 2: 20}, {3: 30, 4: 40})
