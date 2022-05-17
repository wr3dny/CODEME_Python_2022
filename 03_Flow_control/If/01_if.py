season = input('podaj porę roku:')

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')


#1
print('\nPoproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez \n '
      'użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat \n'
      '“Twoja liczba jest podzielna przez 3”.')

x = int(input('Podaj lioczbę:'))
if x % 3 == 0:
    print('podzielna')
else:
    print('niepodzielna')

#3
print('\nStwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. '
      'W zależności od wyniku dodaj komunikaty\n.'
      ' Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.\n')

heroes = int(input('Rate heroes: '))
story = int(input('Rate story'))
lenght = int(input('Rate lenght: '))

rate = (heroes + story + lenght) / 3

if rate >= 7:
    print('Worth of Your time')
elif rate >= 5:
    print('Could be better')
else:
    print('Unworthy piece of paper')