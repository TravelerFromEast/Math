# Fermat Number Sequence
fn_list = []
num = int(input("Enter a number: "))

for i in range(num):
    temp1 = pow(2, i)
    temp2 = pow(2, temp1) + 1
    fn_list.append(temp2)

print(fn_list)