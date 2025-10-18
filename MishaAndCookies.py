n = int(input())
array = input().split()


array = list(map(int,array))

c = 0
t=0
sc = 0
st = 0


for i in range(n):
    if int(array[i]) % 2 == 0:
        c += 1
        sc += i
    else:
        t+=1
        st += i

if c == 0 or t == 0:
    print(0)
else:
    neg = 0
    if sc/c < (n-1)/2:
        neg = (c-1)*c/2
        print(int(sc-neg))
    
    else:
        neg = (t-1)*t/2
        print(int(st-neg))
