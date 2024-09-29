# Deficit number sequence or Defective number sequence
dn_list = []
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum += j
    if sum < 2 * i:
        dn_list.append(i)

print(dn_list)