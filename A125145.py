# A125145

def a(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 3*(a(n - 1) + a(n - 2))

num = int(input("Enter the number of terms: "))
for i in range(num):
    print(a(i), end='\t')
print('\n')