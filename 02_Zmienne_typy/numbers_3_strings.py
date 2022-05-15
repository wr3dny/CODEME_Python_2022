numbers = '352687'
mixed = 'jfioj89wg8w'

print(f'Ciąg {numbers} zawiera same cyfry', numbers.isdigit())
print(f'Ciąg {mixed} zawiera same cyfry', mixed.isdigit())

txt = 'Mata'
centered_txt = txt.center(10, '*')
print(centered_txt)

# ---
url = 'www.example.com'
cut_url = url.lstrip('w')
print(cut_url)


#----

password = 'AdminAdminTakNieRobHasla'

incluedes_at_least_1_upper = password.isalpha() and (not password.islower() and not password.isupper())

print(incluedes_at_least_1_upper)

#----
fruit = 'banana'

counter = fruit.count('na')

print(counter)