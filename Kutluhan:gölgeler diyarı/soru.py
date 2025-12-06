def solve():
    # Test case sayısı (t)
    t = int(input())

    for _ in range(t):
        # Her test case için N ve D değerlerini al
        N, D = map(int, input().split())
        
        monsters = []
        total_enemy_damage = 0
        possible = True
        
        # N tane canavar verisini okumak
        for _ in range(N):
            A, B, C = map(int, input().split())
            
            # Eğer bu grup zaten imkansız (-1) olarak işaretlendiyse
            # sadece okumuş olmak için okuduk, işlem yapmadan geçiyoruz.
            if not possible:
                continue
            
            total_enemy_damage += B
            
            # --- Hesaplama Kısmı ---
            turns = 0
            
            # 1. Durum: Tek vuruşta ölüyor mu?
            if A <= D:
                turns = 1
            else:
                # 2. Durum: Ölmüyor ve iyileşmesi vuruşumuzdan fazla (ÖLÜMSÜZ)
                if C >= D:
                    possible = False
                    continue # Bu satırı okuduk, sıradakine geç.
                
                # 3. Durum: Normal Savaş (Matematiksel Formül)
                remaining_hp = A - D
                net_damage = D - C
                # Yukarı yuvarlama formülü: (Pay + Payda - 1) // Payda
                turns = 1 + (remaining_hp + net_damage - 1) // net_damage
            
            # Listeye [Tur Sayısı, Hasar] olarak ekle
            monsters.append((turns, B))

        # Döngü bitti, sonucu yazdır
        if not possible:
            print("-1")
        else:
            # STRATEJİ: (Tur / Hasar) oranı küçük olanı önce öldür.
            # Yani: Hızlı ölen ama çok vuran her zaman önceliklidir.
            monsters.sort(key=lambda x: x[0] / x[1])
            
            total_damage_taken = 0
            current_total_damage = total_enemy_damage
            
            for turns, damage in monsters:
                # Biz seçtiğimiz canavara saldırırken (turns kadar süre geçer),
                # SEÇMEDİĞİMİZ diğer canavarlar bize vurur.
                
                # Diğerlerinin hasarı = (O anki Toplam Hasar) - (Saldırdığımızın Hasarı)
                others_damage = current_total_damage - damage
                
                # Bu aşamada yediğimiz hasar
                total_damage_taken += others_damage * turns
                
                # Canavar öldü, artık toplam hasar havuzundan gücünü düşüyoruz
                current_total_damage -= damage
                
            print(total_damage_taken)

solve()
