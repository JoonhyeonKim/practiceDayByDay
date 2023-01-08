def solution(numbers):
    answer = 0
    products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            products.append(numbers[i]*numbers[j])
            
    s = sorted(products, reverse=True)
    answer = s[0]
    return answer
