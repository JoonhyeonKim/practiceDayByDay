def solution(n, k):
    answer = 0
    redun = (n//10)
    meal = n*12000
    drink = k*2000
    disc = redun*2000
    answer = meal + drink - disc
    return answer
