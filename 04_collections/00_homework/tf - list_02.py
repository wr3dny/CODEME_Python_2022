# 2 Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
numbers = input("Podaj 10 liczb oddzielonych spacją -> ")
numbers = str(numbers.split())
numbers = int(numbers)
for i in numbers:
    if i %2 != 0:
        print(i)

#if len(elements) %2 == 0:
 #   print('Czy środkowe są takie same są takie same ->', elements[middle] == elements[middle_minus])
#else:
 #   print('Nieparzysta ilość elementów')