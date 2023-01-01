def solution(my_string):
    answer = []
    l = []
    for i in range(10):
        for j in range(len(my_string)):
            if str(i) == my_string[j]: ## different data type cannot be compared unless php
                l.append(i)
    s = sorted(l)
    answer = s
    return answer
  
  ## I found the answer that uses regex
  
import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))
