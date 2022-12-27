def solution(num_list):
    answer = []
    counter_e = 0
    counter_o = 0
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            counter_e += 1
        elif num_list[i]%2==1:
            counter_o += 1
            
    answer.append(counter_e)
    answer.append(counter_o)
            
    return answer
