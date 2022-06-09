# 1
import random

def get_quote(filename):
    with open(f'{filename}.txt', encoding='utf-8') as f:
        content = f.readlines()
    random_random = random.choice(content)
    return random_random

def show(quote):
    quote = quote.strip('\n')
    quote = quote.split(' - ')
    lenght = len(quote[0])
    print(lenght * '*')
    print(quote[0].center(lenght))
    print(f'~{quote[1]}~'.center(lenght))
    print(lenght * '*')


def main():
    filename = input('Podaj nazwę pliku: ')
    quote = get_quote(filename)
    show(quote)



main()




