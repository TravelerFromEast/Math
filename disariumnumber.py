def f(num):
    num_str = str(num)
    sum = 0
    for x in num_str:
        i = num_str.index(x)
        sum += int(x) ** (i + 1)
    return num == sum

num = int(input("Enter a positive integer: "))
if num >= 0:
    if f(num) == True:
        print(f"{num} -> disarium number")
    else:
        print(f"{num} -> not a disarium number")
else:
    print("please enter a non-negative number")
