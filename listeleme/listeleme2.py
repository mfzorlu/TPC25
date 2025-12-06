adet = int(input())

puanlar = list(map(int, input().split()))



sonuc = []

for grupUzunlugu in range(1, adet + 1):


    max_listesi = []

    for baslangıcDegeri in range(adet - grupUzunlugu + 1):

        pencere = puanlar[baslangıcDegeri : baslangıcDegeri + grupUzunlugu]

        max_listesi.append(max(pencere))


    sonuc.append(min(max_listesi))




for i in range(len(sonuc)):
    print(sonuc[i])