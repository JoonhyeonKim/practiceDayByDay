def solution(cipher, code):
    answer = ''
    decrypt = ''
    for i in range(code-1,len(cipher),code): ## code - 1 for starting point, since list counts from 0
        decrypt += cipher[i]
        
    answer = decrypt
    return answer
  
## other solution

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
