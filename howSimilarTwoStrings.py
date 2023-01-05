def solution(s1, s2):
    answer = 0
    counter = 0
    for e in s1:
        for ee in s2:
            if e == ee:
                counter += 1
    answer = counter
    return answer
