def solution(box, n): ## n is unit length
    answer = 0
    l = []
    a = 1
    for i in range(len(box)):
        l.append(box[i]//n)
    for j in range(len(l)):
        a *= l[j]
    answer = a
    return answer
