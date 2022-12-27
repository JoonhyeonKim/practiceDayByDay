def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        e=my_string[i]*n
        answer += e
    return answer
