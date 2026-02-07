n = int(input())
r=n

if n < 6:
    print(-1)
    
else:
    k = n-3
    l =[2, k, n]
    
    for i in range(r):
        k-=2
        n-=2
        l.append(k)
        l.append(n)
        if k == 1:
            break
    
    l.append(r-1)


    for j in range(r):
        print(l[j], end=" ")

