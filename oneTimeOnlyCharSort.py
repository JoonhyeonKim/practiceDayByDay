def solution(s):
    answer = ''
    s = list(s)
    unique = []
    redun = []
    for x in s:
        if x not in unique and x not in redun:
            unique.append(x)
            redun.append(x)
        elif x in unique and x in redun:
            unique.remove(x)
   
    so = sorted(unique)
    
    for i in range(len(so)):
        answer += so[i]
    print(answer)
    return answer
