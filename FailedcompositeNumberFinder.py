def solution(n):
    answer = 0
    counter = 0
    counter2 = 0
    l = []
    m = []
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j==0:
                l.append(i)
                
        if l.count(i) >= 3: ## I failed to find this one by myself and did len(l) >= 3, thus resulting so many cases. but it should count i only
            counter2 += 1
            
    answer = counter2
   
    return answer
