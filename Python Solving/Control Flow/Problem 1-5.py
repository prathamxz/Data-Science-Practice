#	1.	Print numbers from 1 to 100


# for i in range(1,1001,5):
#     print(i)


# 	2.	Print even numbers from 1 to 100

# for i in range(2,101,2):
#     print(i)


# 	3.	Sum of first N numbers

# n = int(input("Enter N: "))

# total = n * (n + 1) // 2

# print("Sum of first N numbers is:", total)

#  	4.	Find factorial of a number

# import math
# s = int(input("Enter a Number = "))
# a = math.factorial(s)

# print("The factorial of",s,"is",a)

# 	5.	Check if number is prime

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

 	# 6.	Reverse a number

a= int(input("enter a.num = "))

print(a[-1:])
