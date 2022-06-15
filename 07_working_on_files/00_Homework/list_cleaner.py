# made for cleaning list of stuff
def get_list(filename):
    with open(f'{filename}.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()
    return content



def list_to_str(name):
    clean_name = [items.split(' ') for items in name]
    print(clean_name)
    clean_name = [i.strip() for sublist in clean_name for i in sublist]
    print(clean_name)
    clean_name = clean_name.join(' ')
    print(clean_name)

    pass

    # name = quote.join('')
    # quote = quote.strip('\n')
    # return name



def main():
    name_list = input('Give name list: ')
    needed_list = get_list(name_list)
    list_list = list_to_str(needed_list)
    print(list_list)

main()

# def main():
#     filename = input('Give file name: ')
#     content = get_list(filename)
#     result = show(content)
#     print(result)
#
# main()

# def remove_extras(text):
#     for char in ' 1234567890':
#         text = text.replace(char, '')
#
#     text = text.replace('\n', ' ')
#     return text
#
# def save(cardtype, number):
#     with open(f'{cardtype}.txt', 'a') as fopen:
#         fopen.write(f'{number}\n')
#
# def main():
#     filename = input("Your file name: ")
#     quote = get_list(filename)
#     show()
#     remove_extras(quote)
#
# main()