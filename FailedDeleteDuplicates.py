def solution(my_string):
    answer = '' ## https://stackoverflow.com/questions/9841303/removing-duplicate-characters-from-a-string
    a = "".join(dict.fromkeys(my_string)) ## it may make dictionary and take key values, since dict is not allowed to have duplicated keys
    
    answer = a
    return answer
