# A list holds many values inone variable, in order. You write it with square brackets and commas.
# Positions start at 0, just like string and -1 is the last ites
# List can be changed .appends(x) adds to the end, .remove(x) deletes a value, and len(x) is for size

fruits = ['apple', 'banana', 'cherry']

print(fruits[0]) #It will print the first element
print(fruits[-1]) #It will print the last element
fruits.append('Mango') #It will add a mango to the list
fruits.remove('banana') #It will remove banana from the list
print(len(fruits))