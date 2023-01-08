eqs = input('Enter the equations each elelemts separated by space while each equations by comma with space: ').split(', ')

def calculator(eqs):
    an = []
    op = ['+', '-', '*', '/']
    for i in range(len(eqs)):
        eql = []
        ##eql.append(list(eqs[i]))
        eql.append(eqs[i].split(' '))
        for j in range(len(eql)):
            v = int(eql[j][0])
            for k in range(1,len(eql[j])):
            
                if eql[j][k] == '+':
                    v += int(eql[j][k+1])
                elif eql[j][k] == '-':
                    v -= int(eql[j][k+1])
                elif eql[j][k] == '*':
                    v *= int(eql[j][k+1])
                elif eql[j][k] == '/':
                    v /= int(eql[j][k+1])
                    
                else:
                    pass
            an.append(v)
                
    
    return an
    
    
ans = calculator(eqs)
print(ans)
