def tur_hasar_orani(canavar):
    """
    Her canavar için tur/hasar oranını döndürür
    canavar = [tur, hasar]
    """
    tur, hasar = canavar
    return tur / hasar


def kutluhan_savas(N, D, canavarlar):
    """
    N: canavar sayısı
    D: Kutluhan'ın verdiği hasar
    canavarlar: [[Ai, Bi, Ci], ...] formatında liste
    """
    canavar_listesi = []
    toplam_hasar = 0
    mumkun = True

    # Her bir canavarı incele
    for Ai, Bi, Ci in canavarlar:

        
        toplam_hasar += Bi
        tur = 0

        if Ai <= D:
            tur = 1
        else:
            if Ci >= D:
                # Bu canavarı yenmek imkansız
                mumkun = False
                continue

            kalan_can = Ai - D
            net_hasar = D - Ci
            tur = 1 + (kalan_can + net_hasar - 1) // net_hasar  # Yukarı yuvarlama

        # [tur, hasar] olarak listeye ekle
        canavar_listesi.append([tur, Bi])

    if not mumkun:
        return -1

    # Strateji: tur / hasar oranı küçük olan önce
    canavar_listesi.sort(key=tur_hasar_orani)

    toplam_yedigimiz_hasar = 0
    su_anki_toplam_hasar = toplam_hasar

    for tur, hasar in canavar_listesi:
        digerlerinin_hasari = su_anki_toplam_hasar - hasar
        toplam_yedigimiz_hasar += digerlerinin_hasari * tur
        su_anki_toplam_hasar -= hasar

    return toplam_yedigimiz_hasar


# ----------------------------
# Ana giriş ve test case döngüsü
t = int(input())

for _ in range(t):
    N, D = map(int, input().split())
    canavarlar = [list(map(int, input().split())) for _ in range(N)]
    sonuc = kutluhan_savas(N, D, canavarlar)
    print(sonuc)
