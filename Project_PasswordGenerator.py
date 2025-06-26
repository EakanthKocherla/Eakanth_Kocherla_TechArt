import string
import random

# characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
# # Print the list
# print(characters)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

print ("Welcome to Kocherla Password Generator")
req_letters = int(input( "How many letters would you like to have in your password?\n"))
req_numbers = int(input( "How many numbers would you like to have in your password?\n"))
req_symbols = int(input( "How many symbols would you like to have in your password?\n"))

password_list = []

for char in range (0, req_letters):
    password_list.append(random.choice(letters))
    
for char in range (0, req_numbers):
    password_list.append(random.choice(numbers))
    
for char in range (0, req_symbols):
    password_list.append(random.choice(symbols))
    
#print (password_list)
random.shuffle(password_list)
print (password_list)

password = ""
for char in password_list:
    password += char

print (f'Your Password is {password}')
