import statistics

def solution(array):
    answer = 0
    a=statistics.multimode(array)
    if len(a) != 1:
        return -1
    else:
        return a[0]   
        
        
->
without library, I tried:
def solution(array):
    answer = 0
    a=max(set(array), key=array.count)
    print(a)
    return answer
