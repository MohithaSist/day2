a=list(map(int,input().split()))
li=[]
for i in range(min(a),max(a)+1):
    li.append(i)
    if i>0:
        if i not in a:
            print(i)
            break

if (li==a):
    print(max(a)+1)
