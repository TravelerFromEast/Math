# Gopala-Hemachandra sequence
def GH(n, a, b):
    if n == 1:
        return a
    elif n == 2: 
        return b
    else:
        return GH(n - 1, a, b) + GH(n - 2, a, b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
num = int(input("Enter number of terms: "))

print(f"Gopal-Hemachandra sequence for a = {a} and b = {b}",end='\n')

for i in range(1, num + 1):
    print(GH(i,a,b), end='\t')
print('\n')