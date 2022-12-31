def solution(n):
    answer = 0
    counter = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j==n:
                counter += 1
    answer = counter            
    return answer 
    

number pair?? -> then this one must be true: n%j==0 https://www.geeksforgeeks.org/python-program-for-count-pairs-with-given-sum/

-> I failed to solve my own:

def solution(n):
    answer = 0
    counter = 0
    l = []
    for j in range(1,n+1):
        if n%j==0: ## thinking of this again, I realized i does not required at all 
            counter += 1
            l.append([j,n//j])
    print(l)        
    answer = counter            
    return answer 
