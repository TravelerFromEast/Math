# happy number or not
def f(num, memory = []):
    if num == 1:
        return True
    elif num > 1:
        sum = 0
        memory.append(num)
        for x in str(num):
            sum += pow(int(x), 2)
        if sum in memory:
            return False
        else:
            memory.append(sum)
            return f(sum)
 
num = int(input("Enter a positive integr: "))

if num <= 0:
    print("please enter a psoitive integer")
else:
    if f(num) == True:
        print("{} -> a happy number".format(num))
    else:
        print(f"{num} -> a sad number")