def solution(dic1, dic2):
    """Enter code here"""
    ans = {}
    for i in range(0,len(dic1)):
        ans[dic1.keys()[i]]=dic1.values()[i]
    for i in range(0,len(dic2)):
        ans[dic2.keys()[i]]=dic2.values()[i]
    return ans
