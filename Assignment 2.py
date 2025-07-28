# Task 1
a = int(input("Enter Your Number: "))
b = a%2
if b == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# Task 2
sum = 0

for i in range(51):
    sum = sum + i

print("Total of all numbers till 50 is: ",sum)