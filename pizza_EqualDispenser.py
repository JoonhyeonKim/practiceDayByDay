def solution(n):
    answer = 0
    gcd = 1
    for i in range(1, min(n,6)+1):
        if n%i==0 and 6%i==0:
            gcd = i
    lcm=n*6/gcd
    answer=lcm/6 # where each pizza is dispensed by 6 pieces
            
    return answer
