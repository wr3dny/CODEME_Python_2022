# phase 1 : create a knight
class Knight:
    def __init__(self):
        self.hp = 60
        self.xp = 0


    def __repr__(self):
        print(f'Knight: hp={self.hp}, xp={self.xp}')

    def march(self, distance):
        self.distance = distance
        print(f'Knight: I have walked {self.distance}m ')
        self.xp += (distance * 0.2)

    def attack(self):
        print(f'Knight: I have swing my sword')
        self.xp += 0.3


# phase 2 : create an archer
class Archer:
    def __init__(self):
        self.hp = 40
        self.xp = 0
        self.quiver = 24

    def __repr__(self):
        print(f'Archer: hp={self.hp}, xp={self.xp}')

    def march(self, distance):
        self.distance = distance
        print(f'Archer: I have walked {self.distance}m ')
        self.xp += (distance * 0.2)

    def attack(self):
        print(f'Archer: I have shot an arrow')
        self.xp += 0.4
        self.quiver -= 1
        if self.quiver <= 0:
            print('Archer: Out of arrows, cant shot')

# phase 3 : create a warrior
class Warrior:
    def __repr__(self):
        print(f'Warrior: hp: {self.hp}, xp: {self.xp}')
    def march(self,distance):
        self.distance = distance
        print(f'Archer: I have walked {self.distance}m ')





def main():
    gavin = Knight()
    gavin.march(20)
    gavin.attack()
    print(gavin.xp)
    orris = Archer()
    print(orris.quiver)
    orris.attack()
    orris.attack()
    print(orris.quiver)



pass


if __name__ == '__main__':
    main()