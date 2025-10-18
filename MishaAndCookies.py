n = int(input())

l = str(input())
array = l.split()
for i in range(n):
    array[i] = int(array[i])

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
for i in c:
    st += i



neg = 0
if ((sc/n) + n) < n/4:
    for i in range(len(c)):
        neg += i
    print(sc-neg)

if ((st/n) + n) < n/4:
    for i in range(len(t)):
        neg += i
    print(st-neg)
