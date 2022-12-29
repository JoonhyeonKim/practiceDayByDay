def solution(balls, share):
    answer = 0
    diff = balls - share
    factB = 1
    factS = 1
    factM = 1
    for i in range(1,balls+1):
        factB = factB*i
    for j in range(1,share+1):
        factS = factS*j
    for k in range(1,diff+1):
        factM = factM*k
    answer = factB/(factM*factS)
    return answer
  
## literally brute-forcing, not scalable  

import math


def solution(balls, share):
    return math.comb(balls, share)
  
##but other people's answer is not so different
