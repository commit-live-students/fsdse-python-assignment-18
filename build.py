def solution(dict1, dict2):
    dict3 = dict(dict1, **dict2)
    return dict3

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
solution(dict1, dict2)
