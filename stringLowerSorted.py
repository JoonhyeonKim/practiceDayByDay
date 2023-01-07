def solution(my_string):
    answer = ''
    lowerList = list(my_string.lower())
    sl = sorted(lowerList)
    for i in range(len(sl)):
        answer += sl[i]
    return answer
  
  
  ## shorter one
  
  def solution(my_string):
    return ''.join(sorted(my_string.lower()))
