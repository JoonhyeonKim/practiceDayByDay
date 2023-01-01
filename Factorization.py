def solution(n):
    answer = []
    prime = isPrime(n)
    m = []
    
    for i in range(len(prime)):
        if n%prime[i]==0:
            m.append(prime[i])
            
    answer = m
    return answer

def isPrime(n):
    counter = 0
    l = []
    prime = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i%j == 0:
                l.append(i)
        if l.count(i) == 2: ## maybe that i is somehow stored in memory
            prime.append(j) ## since it is the definition of prime number
    
    return prime
  
## sort answer

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
