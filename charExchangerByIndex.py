def solution(my_string, num1, num2):
    answer = ''
    dummy = ''
    word = ''
    my_string = list(my_string)
    dummy = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = dummy
    
    for i in range(len(my_string)):
        word += my_string[i]
    
    answer = word
    return answer
