def solution(n):
    answer = 0
    if n/7 > n//7:
        answer = n//7 + 1
    elif n/7 == n//7:
        answer = n//7
    return answer
