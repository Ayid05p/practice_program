i = 1
while i <= 10:
    print(i)
    i += 1


n = int(input("enter positive integer:"))
total = 0
i = 1
while i <= n:
    total += i
    i +=1
print(f"sum of n natural numbers is {total}")


"""num = int(input("enter a number:"))
psum = nsum = zerocount = 0
while(num != -1):
    if num > 0:
        psum = psum + num
    elif num < 0:
        nsum = nsum + num
    else:
        zerocount = zerocount + 1
        num = int(input("enter a number:"))
print(f"sum of all positive number:{psum}")
print(f"count of zeros {zerocount} ")"""


n = int(input("enter positive number:"))
if n < 0:
    print("please enter a positive number")
else:
    i = 1
    while i != 11:
        print(f"{n} X {i} = {n*i}")
        i = i + 1