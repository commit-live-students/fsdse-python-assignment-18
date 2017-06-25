def solution(dic1, dic2):
    """Enter code here"""

    dconcat = dict(dic1) #Creating a dictionary with dic1 as an input and the dict construct
    dconcat.update(dic2) #Updating the dictionary

    return dconcat 
