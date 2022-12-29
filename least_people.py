def solution(hp):
    answer = 0
    remainder = 0
    g = 5
    p = 3
    w = 1
    if hp >= 5:
        answer += hp//g
        remainder += hp%g
        if remainder >= 3:
            answer += remainder//p
            remainder = remainder%p
            answer += remainder
        elif remainder < 3:
            answer += remainder
    elif hp >= 3 and hp < 5: 
        answer += hp//p
        remainder += hp%p
        answer += remainder
    elif hp >= 1 and hp < 3:
        answer += hp
    else:
        answer = 0
            
    return answer
