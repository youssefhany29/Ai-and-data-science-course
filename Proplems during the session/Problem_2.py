num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("is divisible by both 2 & 3")
elif num % 2 == 0:
    print("is divisible by 2")
elif num % 3 == 0:
    print("is divisible by 3")
else:
    print("is not divisible by both")