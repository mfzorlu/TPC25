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


neg = 0
if sc/c < (n-1)/2:
    for i in range(c):
        neg += i
    print(sc-neg)

else:
    for i in range(t):
        neg += i
    print(st-neg)
