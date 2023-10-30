# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
'''
Menu
-------------
1. Encode
2. Decode
3. Quit
Please enter an option: 1
Please enter your password to encode: 12345555
Your password has been encoded and stored!
Menu
-------------
1. Encode
2. Decode
3. Quit
Please enter an option: 2
The encoded password is 45678888, and the original password is 12345555.
4
PROGRAMMING FUNDAMENTALS 1
Lab 6: Software Engineering
Menu
-------------
1. Encode
2. Decode
3. Quit
Please enter an option: 3
'''
def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

#Alejandro Fluitt
def Encode(password):
    new_password = ''
    num = 0
    for i in password:
        num = int(i) + 3
        new_password += str(num)[-1]
    return new_password

def Decode(password):
    old_password = ''
    num = 0
    for i in password:
        num = int(i) + 7
        old_password += str(num)[-1]
    return old_password

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        menu()
        user_input = input('Please enter an option: ')
        if user_input == '1':
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            password = Encode(password)

        elif user_input == '2':
            print(f'The encoded password is {password}, and the original password is {Decode(password)}')
        elif user_input == '3':
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
