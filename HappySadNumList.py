# creating list of happy numbers and sad numbers

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

num = int(input("Enter a positive number: "))

if num <= 1:
    print("please enter a positive integer greater than 1.")
else:
    hap_num = []
    sad_num = []
    print("Happy numbers:")
    for i in range(1, num):
        if f(i) == True:
            hap_num.append(i)
        else:
            sad_num.append(i)
    
    print("List of happy numbers: \n", hap_num)
    print("List of sad numbers: \n", sad_num)
