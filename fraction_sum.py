def solution(denum1, num1, denum2, num2):
    answer = []
    num3 = num1*num2
    n_denum1 = denum1*num2
    n_denum2 = denum2*num1
    n_denum3 = n_denum1+n_denum2
    gcd = 1
    for i in range(1,(min(num3,n_denum3)+1)):
        if num3%i==0 and n_denum3%i==0: # Greatest Common Divisor
            gcd = i

    answer = [n_denum3//gcd, num3//gcd] # where num3//gcd==lcm

    return answer
