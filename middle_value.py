def solution(array):
    answer = 0
    a = 0
    for i in range(1,len(array)):
        if array[i-1]>=array[i]:
            a=array[i-1]
            array[i-1]=array[i]
            array[i]=a
        else:
            pass
    
    mid=array[len(array)//2]
            
    ##answer = sorted[int(len(array)/2)]
    return mid
    
    
def solution(array):
    answer = 0
    l=array
    l.sort()
    mid = len(l)//2
    answer=l[mid]
            
    ##answer = sorted[int(len(array)/2)]
    return answer   
