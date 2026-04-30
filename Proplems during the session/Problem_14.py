# write a program to calculate the length of a string using 2 ways
s = "Hello"
count = len(s)
print(count)
##############
print("-"*10)

s = "Hello"
count = 0
for i in s:
    count+=1
print(count)
##############
print("-"*15)

#Q2
def string(s):
    if len(s) < 2:
        return "Empty String"
    else:
        return s[0:2] + s[-2:]
    
print(string("Hello"))
print(string("H"))

#Q3
print("-"*15)

def String(s):
    if len(s) < 3:
        return s
    elif s[-3:] == "ing":
        return s[:-3] + "ly"
    else:
        return s + "ing"

print(String("play"))
print(String("playing"))
print(String("hi"))

# Q4
print("-"*15)

lst = ["Maro", "youssef", "Hossam", "Hassan", "Huss"]

large_name = [0]

for n in lst:
    if len(n) > len(large_name):
        large_name = n
    
print(f"Largest Name: {large_name}, Length of it: {len(large_name)}")

# Q5
print("-"*15)

s = "Hello"

print(s[-1] + s[1:-1] + s[0])

def swap_first_last(s):
    if len(s) <2:
        return s
    return s[-1] + s[1:-1] + s[0]

print(swap_first_last("Youssef"))

# Q6 
print("-"*15)

def func(k, lst):
    freq = []   
    for i in lst:
        if k < lst.count(i) and i not in freq:
            freq.append(i)
    
    return freq

lst = list(input("Enter the numbers: ").split())
k = int(input("Enter the numbers: "))        

print(func(k, lst))