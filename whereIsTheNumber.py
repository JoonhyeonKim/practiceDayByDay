def solution(num, k):
    answer = 0
    a = -1
    l = list(str(num))
    redun = []
    for i in range(len(l)):
        if l[i] == str(k) and l[i] not in redun:
            a = i+1
            redun.append(l[i])
        
    answer = a
            
    return answer
  

  ## shorter answer
  
  def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
