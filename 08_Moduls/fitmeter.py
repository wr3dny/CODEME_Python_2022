import bmi

def what_now():
    if final == 'niedowaga':
        with open('skinny.txt', 'r') as f:
            content = f.read()
    elif final == 'norma':
        with open('ok.txt', 'r') as f:
            content = f.read()
    elif final == 'nadwaga':
        with open('little_to_fat.txt', 'r') as f:
            content = f.read()
    elif final == 'otyłość':
        with open('fatty.txt', 'r') as f:
            content = f.read()
    return content




def main():
    print(bmi)


main()


