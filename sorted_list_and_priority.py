def solution(emergency):
    answer = []
    a = emergency
    e = emergency
    e=sorted(e) ## when I use e.sort() it changes a too! Thus resulting wrong answer.
    e=e[::-1]

    for i in range(len(a)):
        for j in range(len(e)):
            if a[i] == e[j]:
                answer.append(j+1)
                
    
    return answer
