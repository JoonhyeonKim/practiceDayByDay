def solution(array):
    answer = []
    test = []
    for i in range(len(array)):
        test.append([array[i], i])
    s = sorted(test, reverse=True)
    a = s[0]
    answer = a
    return answer
