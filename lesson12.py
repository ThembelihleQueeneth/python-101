
num = int(input('Please enter a number: '))

for i in range(1,30):
    if num%3==0 and num%5==0:
        print('FizzyBuzz')
        break
    
    elif num%5 == 0 :
        print('Buzz')
        break
    elif num%3==0 :
        print('Fizz')
        break
    else:
        print(num,'is no divisible by either')   
        break    