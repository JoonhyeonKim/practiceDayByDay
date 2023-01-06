def solution(n, numlist):
    answer = []
    l = []
    for num in numlist:
        if int(num) % int(n) == 0:
            l.append(num)
    
    answer = l
    return answer
