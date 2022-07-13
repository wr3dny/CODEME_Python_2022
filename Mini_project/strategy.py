from units.archer import Archer
from units.knight import Knight

knights = []
archers = []


for _ in range(4):
    knights.append(Knight())

print(knights)

# knights.append(Knight())

for Knight in knights:
    Knight.march(2000)

# knights.append(Knight())

for Knight in knights:
    Knight.attack()

print(knights)


for _ in range(3):
    archers.append((Archer(50)))


print(archers)

army = knights + archers


for warrior in army:
    warrior.attack()

print(army)


def main():
    pass


if __name__ == '__main__':
    main()

