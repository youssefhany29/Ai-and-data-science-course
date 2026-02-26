user = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

if user == "admin" and age >= 18:
    print("Welcome Admin")
elif user != "admin" and age >= 18:
    print("Welcome User")
else:
    print("You are too young")