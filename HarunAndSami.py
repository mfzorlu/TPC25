liste = input()
a,b = map(int,liste.split())

c = input()

harun = 0
sami = 0



for i in c:
    if i == "H":
        harun +=1
    else:
        sami +=1

if harun > a/2:
    print("Harun")
elif sami > a/2:
    print("Sami")
else:
    print("Cilek")
