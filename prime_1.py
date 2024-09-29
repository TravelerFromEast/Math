num = int(input("Enter a number: "))

for i in range(2, num + 1):
    count = 0
    n = int(pow(i,0.5))
    for j in range(1, n + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i, end='\t')
