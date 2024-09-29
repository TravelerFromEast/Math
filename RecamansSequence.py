#Recamán's sequence 
r_list = []

num = int(input("Enter a number: "))

for i in range(num):
    if i == 0:
        r_list.append(i)
    else:
        temp = r_list[i - 1] -  i
        if temp > 0 and temp not in r_list:
            r_list.append(temp)
        else:
            temp = r_list[i - 1] + i
            r_list.append(temp)

print(r_list)