def solution(array):
    answer = 0
    l = []
    counter = 0
    s = ''.join(map(str,array))
    for i in range(len(s)):
        l.append(s[i])
    for j in range(len(l)):
        if l[j] == str(7):
            counter += 1
    answer = counter
    return answer
