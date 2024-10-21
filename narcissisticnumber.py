def f(num):
    num = str(num)
    d = len(num)
    sum = 0
    for x in num:
        sum += int(x) ** d
    if sum == int(num):
        return True
    return False

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("please enter a non-negative integer")
else:
    if f(num) == True:
        print("{} -> Narcissistic number".format(num))
    else:
        print(f"{num} -> not a narscissistic number")