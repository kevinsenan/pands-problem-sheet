# accounts.py
# week 3 task. User enters 10 char acc number, ouput the last four digits and the rest as X
# author K Donovan

#request user to enter acc number
account_number = input("Please enter 10 digit account number:")

#get the numbers from 7 to 10
last_four = (account_number[6:10])

#put 6 X into variable x_string
x_string = 'XXXXXX'

#concatenate X's and last numbers
obfuscated = x_string + last_four
print(obfuscated)


#to print any length assuming there is always at least 4, get the length of account number
length_of_acc_num = len(account_number)

#for a while loop, take 4 from the length of the account number
num_of_x = length_of_acc_num - 4

#use a while loop to increment the number of X's in the variable to append
insert = 'X'
to_append = 'X'

while num_of_x <= length_of_acc_num:
    to_append += insert
    length_of_acc_num -= 1
    #num_of_x -= 1

obfuscated2 = to_append + last_four  
print(obfuscated2)