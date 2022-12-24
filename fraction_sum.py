def solution(denum1, num1, denum2, num2):
    answer = []
    if num1 != num2:
        gcd = 1 # by default, gcd = 1
        for i in range(1,int(min(num1,num2)+1)):
            if num1%i==0 and num2%i==0: # Greatest Common Divisor
                gcd = i
        num3 = num1*num2
        n_denum1 = denum1*num2
        n_denum2 = denum2*num1
        n_denum3 = n_denum1+n_denum2
        answer = [n_denum3//gcd, num3//gcd]
    else:
        denum3 = denum1+denum2
        answer = [denum3, num1]
    return answer
