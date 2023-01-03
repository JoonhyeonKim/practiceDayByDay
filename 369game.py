def solution(order):
    answer = 0
    cl = ['3', '6', '9']
    count = 0
    for i in range(len(str(order))):
        if str(order)[i] in cl:
            count += 1
    answer = count
    
    return answer
