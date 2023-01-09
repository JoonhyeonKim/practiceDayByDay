def solution(sides):
    answer = 0
    answer = 2*min(sides) - 1
    return answer
  
## there're two cases:
##b < a+c
##or
##c < a+b
##then

##b-a < c < a+b

##then max - min + 1 is the num of c
##such that
##2a-1
##where a is min of sides
