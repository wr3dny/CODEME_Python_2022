#Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty. Funkcja zapisująca do pliku
# chroni przed nadpisaniem istniejącego pliku.
import os
def filenamer():
    filename = input('Give Your file name: ')
    return filename

def checker(name):
    try:
        with open(f'{filename}.txt, w') as f:
           content = f.read()
    except FileExistsError:
        print('Plik już istnieje')
        print(content)

def main():
    filename = filenamer()
    print(filename)
    # checker(filename)

main()
