n = int(input())
array = input().split()


array = list(map(int,array))

c = []
t = []

for i in range(n):
    if int(array[i]) % 2 == 0:
        c.append(i)
    else:
        t.append(i)


sc = 0
for i in c:
    sc += i
st = 0
for i in t:
    st += i



neg = 0
if sc/len(c) < (n-1)/2:
    for i in range(len(c)):
        neg += i
    print(sc-neg)

else:
    for i in range(len(t)):
        neg += i
    print(st-neg)
