def solution(n):
    answer = 0
    l = list(str(n))
    sum = 0
    for n in l:
        sum += int(n)
    answer = sum    
    return answer
