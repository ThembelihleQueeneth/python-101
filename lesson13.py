myself = {
    "name":"Thembelihle",
    "age":24,
    "city":"Polokwane Luthuli 9L",
    "hobby":"Coding"
}

myself["carrer"] = "AI Engineer"
myself["hobby"] = "Reading"

for key, value in myself.items():
    print(key, " = ",value)
    
key = input("Please Enter a key: ")

result = myself.get(key)

if result is not None:
    print("Value: ", result)
else:
    print("Sorry, that key does not exist")     
    