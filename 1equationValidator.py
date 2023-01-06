def solution(quiz):
    answer = []
    eq = []
    an = []
    tf = []
    
    for equation in quiz:
        e = list(equation.split('='))
        eq.append(e[0])
        an.append(e[1])
        
    for i in range(len(eq)):
        if eval(eq[i]) == int(an[i]):
            tf.append("O")
        else:
            tf.append("X")
        
    
    
    answer = tf  
    return answer
  
  
  ##Of course you should not use eval 
  
  def solution(quiz):
    answer = []
    for q in quiz:
        eq,ans = q.split(' = ')
        a,op,b = eq.split() ## this one is the thing I did not think of
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer
