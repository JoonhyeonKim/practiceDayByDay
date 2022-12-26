def solution(n):
    answer = 0
    gcd = 1
    for i in range(1, min(n,6)+1):
        if n%i==0 and 6%i==0:
            gcd = i
    lcm=n*6/gcd
    answer=lcm/6 # where each pizza is dispensed by 6 pieces, then it is (n/gcd) * (6/gcd)
            
    return answer

# question was, when pizza is sliced by 6 pieces, what are the least amount pizzas(n) that are required for people to have equal piece(s)
#->
#thus one needs to do divide by gcd(least)
#since the amount of chunks one recieves is not something that matters: people/gcd(people,pieces)*pieces/gcd(people,pieces)
