# Practice makes it perfect
# inzva community built algoleague for every algorithm enthusiast hungry 
# for self-improvement and friendly competition. Have fun and good luck!

n = int(input())
array = str(input())
array = array.split()

result = 0
c = int(array[0])

for i in range(1,n):
    if int(array[i]) > c:
        c = int(array[i])
        result += 1

print(result)
