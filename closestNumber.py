def solution(array, n):
    answer = 0
    l = []
    for i in range(len(array)):
        l.append([abs(array[i]-n),array[i]])
    
    s = sorted(l)
    a = s[0][1]
    answer = a
    return answer
