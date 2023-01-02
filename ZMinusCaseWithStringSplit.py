def solution(s):
    answer = 0
    sum = 0
    t = s.split(' ') ## string.split('delimiter') can be assigned to variable as a list
    
    
    for i in range(len(t)):
        if t[i] == "Z":
            sum -= int(t[i-1])
        else:
            sum += int(t[i])
        
    answer = sum
        
    return answer 
