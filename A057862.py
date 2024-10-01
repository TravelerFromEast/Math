# A057862
# a(n) = 2^n mod Fibonacci(n).
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

def a(n):
    return pow(2,n) % f(n)

num = int(input("Enter the number of terms: "))
for i in range(1, num+1):
    print(a(i), end='\t')
print('\n')