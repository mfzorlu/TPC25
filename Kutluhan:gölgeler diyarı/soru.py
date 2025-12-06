def solve():
    t = int(input())

    for _ in range(t):
        N, D = map(int, input().split())

        canavarlar = []
        toplam_hasar = 0
        mumkun = True

        for _ in range(N):
            A, B, C = map(int, input().split())
            if not mumkun:
                continue

            toplam_hasar += B
            tur = 0

            if A <= D:
                tur = 1
            else:
                if C >= D:
                    mumkun = False
                    continue

                kalan_can = A - D
                net_hasar = D - C
                tur = 1 + (kalan_can + net_hasar - 1) // net_hasar

            canavarlar.append((tur, B))

        if not mumkun:
            print("-1")
        else:
            canavarlar.sort(key=lambda x: x[0] / x[1])

            toplam_yedigimiz_hasar = 0
            su_anki_toplam_hasar = toplam_hasar

            for tur, hasar in canavarlar:
                digerlerinin_hasari = su_anki_toplam_hasar - hasar
                toplam_yedigimiz_hasar += digerlerinin_hasari * tur
                su_anki_toplam_hasar -= hasar

            print(toplam_yedigimiz_hasar)

solve()
