def solution(polynomial):
    answer = ''
    l = polynomial.split(' ')
    coef = 0
    num = 0
    eq = ''
    for element in l:
        if element != '+' and 'x' in element:
            if element[:-1] == '':
                coef += 1
            else:
                coef += int(element[:-1]) 
                
        elif element != '+' and 'x' not in element:
            num += int(element)
    
    if int(coef) == 1:
        coef = ''
        
    if num != 0 and str(coef) != '0':    
        eq = str(coef)+'x'+' + '+str(num)
    elif num != 0 and str(coef) == '0':
        eq = str(num)
    elif num == 0 and str(coef) != '0':
        eq = str(coef)+'x'
    else:
        eq = ''
    
    answer = eq
    
    return answer
