#A155020

def a(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 2*(a(n - 1) + a(n - 2))

num = int(input("Enter the number of terms: "))
for i in range(num):
    print(a(i), end='\t')
print("\n")