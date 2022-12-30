def solution(numbers, k):
    answer = 0
    l=[]
    if k*3 >= len(numbers):
        l.append(k*numbers)
        l = l[0]
    answer=l[2*(k-1)] ## 2 for step size
    
    return answer
##better one

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)] ## such that I don't have to append list and strip it
