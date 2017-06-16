def solution(dic1, dic2):
    """Enter code here"""
    dic3 = dict(dic1) #Creating a dictionary with dic1 as an input and the dict construct
    dic3.update(dic2) #Updating the dictionary

    return dic3
