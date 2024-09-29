# primorial
# denoted by "#", is a function from natural numbers to natural numbers similar to the factorial function, 
# but rather than successively multiplying positive integers, the function only multiplies prime numbers. 
# - Wikipedia
p_list = []
num = int(input("Enter a number: "))

for i in range(2, num):
    val = int(pow(i, 0.5))
    count = 0
    for j in range(1, val + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        p_list.append(i)

print(f"List of prime numbers upto {num}", end='\n')
print(p_list)

pm_list = []
for i in range(len(p_list)):
    mult = 1
    for j in range(0, i + 1):
        mult *= p_list[j]
    pm_list.append(mult)

print(end='\n')
print("List of primorials for the above list of primes", end='\n')
print(pm_list)
