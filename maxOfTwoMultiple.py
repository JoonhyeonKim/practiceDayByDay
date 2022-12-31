def solution(numbers):
    answer = 0
    l = []
    for i in range(len(numbers)):
        for j in range(1,len(numbers)-i): ## such that at max, index should be len(number)-1
            e = numbers[i]*numbers[i+j]
            l.append(e)
    s = sorted(l)
    s = s[::-1]
    answer = s[0]
    return answer
  
  
  ##but this one is elegant
  
  def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
