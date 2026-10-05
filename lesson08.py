age = int(input('Enter your age: '))

isStudet = input('Are you a student: ')

price1 = 5
price2 = 8
price3 = 6
price4 = 12

if age < 12:
    print(f"Your ticket price is R{price1} ")
elif isStudet == 'Yes':
    print(f"Your ticket price is R{price2}")  
elif age > 65:
    print(f"Your ticket price is R{price3}")   
else:
    print(f"Your ticket price is R{price4}")       