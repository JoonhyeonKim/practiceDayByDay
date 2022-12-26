def solution(money):
    answer = []
    IAP = 5500
    amount=money//IAP
    rest=int(money - amount*IAP)
    answer.append(amount)
    answer.append(rest)
    return answer
