def solution(my_string):
    answer = 0
    a = eval(my_string)
    answer = a
    return answer
  
  
## But we all know that eval is dangerous function

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
  
