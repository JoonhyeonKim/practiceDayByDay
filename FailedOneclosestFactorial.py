from math import factorial

def solution(n):
    answer = 0
    i = 10
    while n<factorial(i):
        i -= 1
    
    answer = i
    return answer
