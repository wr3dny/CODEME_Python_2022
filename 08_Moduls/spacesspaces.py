from spaces import square_rund, rounded, space

def main():
    choice = square_rund()
    if choice == 'y':
        a = int(input('One size: '))
        b = int(input('Second size: '))
        print(space(a, b))
    else:
        r = int(input('Radius'))
        print(rounded(r))

main()