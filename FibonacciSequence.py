# Fibonacci Sequence

f_list = [1, 1]

num = int(input("Enter a number: "))

for i in range(2, num):
    f_list.append(f_list[i - 1] + f_list[i - 2])

print(f_list)