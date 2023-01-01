def solution(my_string):
    answer = ''
    v = ['a', 'e', 'i', 'o', 'u']
    mn = my_string ## newly assigned for recursion
    
    for i in range(len(v)):
        if v[i] in my_string:
            mn = mn.replace(v[i], "") ##useful string or list methods: replace, sort, pop, remove, append, while new=sorted(list) also new=mystring.replace("a","b") https://www.freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python/ 
    
            
    answer = mn
    return answer
