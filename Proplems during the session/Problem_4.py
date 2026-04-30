# find second greatest number

lst = [10, 20, 30, 40, 90, 100, 5]

max_num = lst[0]
sec_num = lst[1]

for num in lst:
    if num > max_num:
        sec_num = max_num
        max_num = num
    elif num > sec_num:
        sec_num = num

print(max_num)
print(sec_num)