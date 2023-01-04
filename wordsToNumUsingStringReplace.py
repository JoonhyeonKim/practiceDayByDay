def solution(numbers):
    answer = 0
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(num)):
        if num[i] in numbers:
            numbers = numbers.replace(num[i], str(i)) ## string's replace method
    answer = int(numbers) 
    return answer
