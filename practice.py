a = int(input("enter first number:"))
b = int(input("enter second number:"))
sum = a + b
print(sum)

number = []
print("enter 10 numbers:")
for i in range(10):
    user_input = input("enter the number")
    number.append(float(user_input))
print(number)
total_sum = sum(number)
print("the sum is:", total_sum)