def solution(num_list, n):
    answer = []
    l = []
    for i in range(0,len(num_list), n): ## it jumps by n length till len(num_list)-1
      answer.append(num_list[i:i+n]) ## it adds by n length of element
    
    return answer
