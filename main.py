print('Welcome to Password_Generator')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','^']

import random
password = ''

no_of_numbers=int(input('No. of numbers do you want :'))
no_of_symbols=int(input('No. of symbols do you want :'))
no_of_letters=int(input('No. of letters do you want :'))

list_of_computer_selected_numbers=[]
list_of_computer_selected_symbols=[]
list_of_computer_selected_letters=[]

for i in range(0,no_of_numbers):
    i=random.choice(numbers)
    list_of_computer_selected_numbers.append(i)

for i in range(0,no_of_symbols):
    i=random.choice(symbols)
    list_of_computer_selected_symbols.append(i)

for i in range(0,no_of_letters):
    i=random.choice(letters)
    list_of_computer_selected_letters.append(i)   

Un_Shuffled_list=list_of_computer_selected_numbers+list_of_computer_selected_symbols+list_of_computer_selected_letters

Shuffled_list=random.sample(list_of_computer_selected_numbers+list_of_computer_selected_symbols+list_of_computer_selected_letters,len(list_of_computer_selected_numbers+list_of_computer_selected_symbols+list_of_computer_selected_letters))

User_comfort=int(input('Do you want a simple(0) password or a complicated(1) :'))

if User_comfort==0:
    for i in Un_Shuffled_list:
        password+=i
else:
    for i in Shuffled_list  :
        password+=i 

print(password)


    