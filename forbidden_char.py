def solution(my_string, letter):
    answer = ''
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == letter:
            my_string[i] = ''
            answer += my_string[i]
        else:
            answer += my_string[i]
    return answer
