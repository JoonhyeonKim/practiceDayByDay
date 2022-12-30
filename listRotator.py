def solution(numbers, direction):
    answer = []
    
    
    if direction=="left":
        e=numbers.pop(0)
        numbers.append(e)
    if direction=="right":
        c=numbers.pop(len(numbers)-1)
        numbers.insert(0,c)
      
    answer = numbers    
    return answer
