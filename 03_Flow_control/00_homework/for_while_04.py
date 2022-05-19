# 4 Napisz grę - kamień (k) / papier (p) / nożyce (n).

import random

CPU_choice = random.choices(['k', 'n', 'p'])


player_score = 0
player_choice = input('Podaj swój wybór k/n/p: ')


if CPU_choice == player_choice:
    print('It\'s a draw')
elif (CPU_choice == 'k' and player_choice == 'p') or (CPU_choice == 'n' and player_choice == 'k') or (CPU_choice == 'p' and player_choice == 'n'):
    print('Player, You won !')
