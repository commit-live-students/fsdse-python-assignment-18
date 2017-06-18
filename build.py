def solution(dic1, dic2):
    dictionary = dict(dic1)
    dictionary.update(**dic2)
    return dictionary
