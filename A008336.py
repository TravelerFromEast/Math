#Alternate Sequence by Recamán
ar_list = [1]
num = int(input("Enter a number: "))

for i in range(1, num):
    if ar_list[i - 1] % i == 0:
        val = int(ar_list[i - 1]/i)
        ar_list.append(val)
    else:
        val = i * ar_list[i - 1]
        ar_list.append(val)

print(ar_list)