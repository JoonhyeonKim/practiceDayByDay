def solution(array, height):
    answer = 0
    counter = 0
    s = sorted(array, reverse = True) ## array.sort() -> array object is sorted thus object itself is mutated, sorted(array) -> array variable is sorted
    for i in range(len(s)):
        if int(s[i]) - height > 0 :
            counter += 1
        else:
          pass
        
    answer = counter 
    return answer
