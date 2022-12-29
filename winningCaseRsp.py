def solution(rsp):
    pair = {'2': '0', '0':'5', '5':'2'}
    rspl = []
    answer = ''
    
    for i in range(len(rsp)):
        rspl.append(rsp[i])
    
    for j in range(len(rspl)):
        for c, w in pair.items():
            if rspl[j] == c:
                answer += w
        
   
    return answer
  ## this time, also I think this is not that efficient answer
  
  def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
