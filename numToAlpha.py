def solution(age):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] ## more general answer should be based on https://www.sololearn.com/discuss/1947743/how-to-get-alphabets-in-order-through-loop-in-python-is-it-possible-of-getting-alphabets-through
    age=str(age)
    age=list(age)
    for i in range(len(age)):
        answer += alpha[int(age[i])]
    
    
    return answer
