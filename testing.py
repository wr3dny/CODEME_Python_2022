if abs(name_lenght % 2 != 0):
    print('You picked and odd number')
    name_length = int(input('Pick up Your number again: '))
else:
    j = 0
    for j in range(0, int(name_lenght / 2)):
        generated_name.append(random.choice(name_parts))
        j += 1