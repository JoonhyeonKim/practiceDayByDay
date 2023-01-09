import re

def solution(my_string):
    numbers = list(map(int,re.findall(r'\d+', my_string)))
    return sum(numbers)
