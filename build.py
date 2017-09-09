def solution(dic1, dic2):
    return dict (dic1, ** dic2)

if __name__ == "__main__":
    print solution ({1: 10, 2: 20}, {3: 30, 4: 40})
    
