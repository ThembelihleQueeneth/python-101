word = input("Please enter a word: ").lower()

vowels = ["a","e","i","o","u"]

count = 0

for letter in word:
    if letter in vowels:
        count+=1
        
        
print(f"Your vowels count is {count}")        