# Catalan number sequence
# A000108 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n - 1)

def C(n):
    num = factorial(2*n)
    dem = factorial(n)*factorial(n+1)
    return int(num/dem)

num = int(input("Enter a number: "))

for i in range(num):
    print(C(i), end='\t')