# determine whether a number is fascinating or not
def f(num):
    num_str = str(num)
    d = len(num_str)
    if d < 3:
        return False
    else:
        num_set = {str(x) for x in range(1, 10)}
        derived_num = num_str + str(num * 2) + str(num * 3)
        derived_set = set(derived_num)

        return num_set == derived_set
           
num = int(input("Enter a number: "))

if not f(num):
    print(f"{num} -> not a fascinating number")
else:
    print(f"{num} -> a fascinating number.")