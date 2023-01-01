def solution(my_string):
    answer = 0
    l = []
    s = 0 
    for i in range(10):
        for j in range(len(my_string)):
            if str(i) == my_string[j]:
                l.append(i)
                
    for k in range(len(l)):
        s +=  l[k]
        
    answer = s
    return answer
  
  ## again more elegant one
  
  def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
