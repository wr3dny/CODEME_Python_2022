# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

norway_names = ['Ingrid', 'Sofia', 'Leah', 'Sofie', 'Emilie', 'Olivia', 'Maja', 'Ella', 'Emma', 'Nora']
belgium_names = ['Olivia', 'Emma', 'Mila', 'Louise', 'Lina', 'Alice', 'Sofia', 'Mia', 'Anna', 'Juliette']
uk_names = ['Olivia', 'Amelia', 'Isla', 'Ava', 'Mia', 'Ivy', 'Lily', 'Isabella', 'Sophia', 'Rosie']
estonia_names = ['Mia', 'Sofia', 'Emily', 'Hanna', 'Nora', 'Emma', 'Eva', 'Alisa', 'Marta', 'Lenna']
finland_names = ['Aino', 'Olivia', 'Sofia', 'Pihla', 'Aada', 'Eevi', 'Isla', 'Lilja', 'Helmi', 'Ella']
italy_names = ['Sofia', 'Giulia', 'Aurora', 'Ginevra', 'Alice', 'Beatrice', 'Emma', 'Giorgia', 'Vittoria', 'Matilde']
moldova_names = ['Sofia', 'Amelia', 'Anastasia', 'Maria', 'Daria', 'Victoria', 'Eva', 'Alexandra', 'Evelina', 'Andreea']
netherlands_names = ['Julia', 'Mila', 'Emma', 'Nora', 'Olivia', 'Sophie', 'Tess', 'Milou', 'Zoë', 'Yara']
romania_names = ['Sofia', 'Amelia', 'Anastasia', 'Maria', 'Victoria', 'Daria', 'Eva', 'Alexandra', 'Evelina', 'Andreea']
switzerland_names = ['Mia', 'Emma', 'Mila', 'Emilia', 'Lina', 'Sofia', 'Elena', 'Lea', 'Alina', 'Laura']

top_ten_names = [norway_names + norway_names + uk_names + estonia_names + finland_names + italy_names + moldova_names +
                 netherlands_names + romania_names + switzerland_names]


norway_names = set(norway_names)
print(norway_names)


#
# top_ten_names.split()
#
# print(top_ten_names)
# ttn = list(set(top_ten_names))
#
#
# names_counter = {}

# for name in top_ten_names:
#     if name in names_counter:
#         names_counter[word] += 1
#     else:
#         names_counter[word] = 1
#
# for k, v in words_counter.items():
#     print(f'- {k} : {v}')
#
# print(top_ten_names)
#print(names_counter)


