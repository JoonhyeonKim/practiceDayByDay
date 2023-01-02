def solution(sides):
    answer = 0
    s = sorted(sides, reverse = True)
    
    if s[0] < (s[1] + s[2]):
        answer = 1
    else:
        answer = 2
    
    return answer
