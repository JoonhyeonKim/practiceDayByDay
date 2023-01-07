def solution(array, n):
    answer = 0
    counter = 0
    for num in array:
        if num == n:
            counter += 1
    answer = counter 
    return answer
  
  ## shorter answer
  
  def solution(array, n):
    return array.count(n)
