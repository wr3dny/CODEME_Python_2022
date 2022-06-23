# 5 Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc,
# kupic, zwrocic.

class Shop:
    items_list = []
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def view(self):
        print(f'A graphic it should be for {self.name}')

    def take_try(self):
        print(f'{self.name} is in trial mode')

    def buy(self):
        print('You have buy ')