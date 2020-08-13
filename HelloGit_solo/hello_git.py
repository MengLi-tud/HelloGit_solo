message ="Hello Delft"
print(message)

a = input("what is your name?")
print("Hi", a, ", Have a great day!")

b = int(input("what is your age?"))
print(f"You are {b} years young!")


#print out all numbers uptil the user's age
for x in range(b):
    print(x+1, end=" ")