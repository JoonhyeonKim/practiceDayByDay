d = input()
for i in range(0,len(d), 2): ##if step was 1 then max of range is len(d)-1, while step is now 2 max of range is len(d)-2
    print(d[i:i+2]) ##thus this one is in the range of index
