# mail_list = ['one@gmail.com', 'two@gmail.com']

with open(mail_list.txt) as fopen:
    content = fopen.readlines()


user_mail = input('Give Your email: ')
while user_mail not in mail_list:
    user_mail = input('Give Your email: ')
else:
    print('Your mail on the list !')

