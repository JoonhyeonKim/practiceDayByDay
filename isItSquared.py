def solution(n):
    answer = 0
    a = 0
    l = []
    for i in range(1,n+1):
        if n/i == i:
            l.append([i, n])
        else:
            a = 2
    
    if len(l) != 0:
        a = 1
    
    answer = a
        
            
    return answer
  ## shorter one
  
  def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2
