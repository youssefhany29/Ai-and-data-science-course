#CodeForces
n = int(input("Enter the numbers of solutions: "))

count = 0

for _ in range(n):
        a,b,c = list(map(int, input("how many solutions: ").split()))
        if a + b + c >= 2:
            count += 1
            
print(f"We have {count} solutions")