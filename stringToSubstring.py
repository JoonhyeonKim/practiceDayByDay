def solution(my_str, n):
    answer = []
    
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    
    return answer
  
 
## shorter answer

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
