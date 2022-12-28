def solution(n):
    answer = 0
    for i in range(0,n+1,2): ## n+1 since n is not included
        answer += i
    return answer
