#create a list of numbers and write a program to sort it in ascending order

lst = [10, 30, 20, 50, 40, 70, 60, 90, 100]

for i in range(len(lst)):
    min_num = i

    for j in range(i +1, len(lst)):
        if lst[j] < lst[min_num]:
            min_num = j
    
    lst[i], lst[min_num] = lst[min_num], lst[i]
    
print(lst)