class programmers_lv1_1:
    def solution(self, bandage, health, attacks):
        t, x, y = bandage
        max_health = health
        current_health = health
        success_time = 0

        attack_dict = {attack[0]: attack[1] for attack in attacks}
        last_time = attacks[-1][0]

        for time in range(last_time + 1):
            if time in attack_dict:
                current_health -= attack_dict[time]
                success_time = 0
                if current_health <= 0:
                    return -1
            else:
                current_health = min(current_health + x, max_health)
                success_time += 1
                
                if success_time == t:
                    current_health = min(current_health + y, max_health)
                    success_time = 0

        return current_health

if __name__ == '__main__':
    rr = programmers_lv1_1()
    bandage = [5, 1, 5]
    health = 30
    attacks = [[1, 15], [5, 16], [8, 6]]
    print(rr.solution(bandage, health, attacks))
