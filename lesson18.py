# Error Handling



while True:
    try:

        n1 = int(input('Enter the first number: '))
        n2 = int(input('Enter the second number: '))
        print(n1/n2)
        break; 
    except ValueError:
        print("That was not a number")
    except ZeroDivisionError:
        print('You cannot divide by zero')     
          
   