# Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie
# kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
# Rozgrywka powinna być maksymalnie intuicyjna.
import random

def random_word():
    with open('fruits.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()
        word = random.choice(content)
        return word

