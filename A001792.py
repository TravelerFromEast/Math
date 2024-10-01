# A001792
# a(n) = (n+2)*2^(n-1). 
def a(n):
    if n == 0:
        return 1
    else:
        return (n + 2)*pow(2, n - 1)

num = int(input('Enter the number of terms: '))
for i in range(num):
    print(a(i), end='\t')
print('\n')