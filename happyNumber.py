# happy number or not
def f(num, memory = None):
    if memory == None:
        memory = set()

    if num == 1:
        return True
    elif num in memory:
        return False
    else:
        memory.add(num)
        sum = 0
        for x in str(num):
            sum += pow(int(x), 2)
        return f(sum,memory)
 
num = int(input("Enter a positive integr: "))

if num <= 0:
    print("please enter a positive integer")
else:
    if f(num) == True:
        print("{} -> a happy number".format(num))
    else:
        print(f"{num} -> a sad number")
