n = int(input()) # How many flags
locationsList = []# List of the locations of the flags
for i in range(n):
    pairs = input()# Locations of the flags
    pairsList = pairs.split()# Split the locations into a list
    pairsList[0] = int(pairsList[0])# Convert the first element to an integer
    pairsList[1] = int(pairsList[1]) # Convert the second element to an integer
    locationsList.append(pairsList) # Add the locations to the list




for i in range(n):
    for j in range(i + 1, n):
        nokta1 = locationsList[i]
        nokta2 = locationsList[j]
        
       
        ort_x = (nokta1[0] + nokta2[0])/2
        ort_y = (nokta1[1] + nokta2[1])/2
        
        kos_uzn = (nokta1[0] - nokta2[0])**2 + (nokta1[1] - nokta2[1])**2
    
        


    #    toplam_dikdortgen += (kosegen sayi * (kosegen sayi - 1)) // 2

print(toplam_dikdortgen)
