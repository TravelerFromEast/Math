# Co-prime sequence
def process(i, j):
    if i % j != 0:
        tp_list.append((i, j))


tp_list = []

num = int(input("Enter a number: "))

for i in range(2, num + 1):
    for j in range(2, num + 1):
        if i < j:
            temp = i
            i = j
            j = temp 
            process(i, j)
        else:
            process(i, j)

print(set(tp_list))

# Why did I introduced swapping in the code? 
# Let us consider the example i = 2 and j = 4, 2 % 4 = 2, not 0 and according to the process function
# i, j pair will bw included in the tp_list. But 2, 4 pair is not prime.
# Therefore, to eliminate this error I introduced swapping.

# set() is introduced to eliminate duplicate elements in tp_list
                    