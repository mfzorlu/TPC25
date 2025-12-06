def solve():
    t = int(input())

    for _ in range(t):
        N, D = map(int, input().split())

        monsters = []
        total_enemy_damage = 0
        possible = True

        for _ in range(N):
            A, B, C = map(int, input().split())
            if not possible:
                continue

            total_enemy_damage += B
            turns = 0

            if A <= D:
                turns = 1
            else:
                if C >= D:
                    possible = False
                    continue

                remaining_hp = A - D
                net_damage = D - C
                turns = 1 + (remaining_hp + net_damage - 1) // net_damage

            monsters.append((turns, B))

        if not possible:
            print("-1")
        else:
            monsters.sort(key=lambda x: x[0] / x[1])

            total_damage_taken = 0
            current_total_damage = total_enemy_damage

            for turns, damage in monsters:
                others_damage = current_total_damage - damage
                total_damage_taken += others_damage * turns
                current_total_damage -= damage

            print(total_damage_taken)

solve()
