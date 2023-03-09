# bank.py
# week 2 task. User enters amounts in cent, add them and print as Euro and cent
# author K Donovan

#Prompt the user for the cent value, convert to int
amount1 = int(input("Enter amount 1 (in cent):"))
amount2 = int(input("Enter amount 2 (in cent):"))
# add the cent values
ans = amount1 + amount2
#divide the values by 100 for euro and cent
value = ans / 100
#format the value to give 2 decimal places to ensure the 0 integer is displayed
asEuro = "{:.2f}".format(value)
print(f"The sum of these is € {asEuro}")