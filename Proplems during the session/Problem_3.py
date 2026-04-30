#Write a function that takes a list of numbers from the user and prints whether each number is even or odd.

def check_even_odd(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

check_even_odd(int(input("Enter some numbers")))