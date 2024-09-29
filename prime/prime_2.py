p_list = [2]

def process(n):
    count = 0
    l = 1
    for j in range(n):
            if i % p_list[j] == 0 or i % p_list[l - j - 1] == 0:
                count += 1
                break 
    if count == 0:
        p_list.append(i)
        l = len(p_list)

num = int(input("Enter a number: "))

for i in range (3, num + 1):
    if len(p_list) % 2 == 0:
        process(len(p_list)//2)
    else:
        process(len(p_list)//2 + 1)

print(p_list)
