dic1 ={1:2,2:3}
dic2= {4:5,5:6}
def solution(dic1, dic2):
    d3 = dict(dic1.items() + dic2.items())
    return d3

d3=solution(dic1,dic2)
print d3
