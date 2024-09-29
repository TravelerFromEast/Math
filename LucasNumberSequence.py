# Lucas number sequence
l_list = [2, 1]
num = int(input("Enter a number: "))

for i in range(2, num):
    l_list.append(l_list[i - 1] + l_list[i - 2])

print(l_list)