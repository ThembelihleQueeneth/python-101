
from datetime import date

message = input('How are you feeling today? ')

with open('note.txt', 'a') as f:
    f.write(message + '\n')

with open('note.txt', 'a') as f:
    f.write(str(date.today()) + '\n')

with open('note.txt', 'r') as f:
    print(f.read())
