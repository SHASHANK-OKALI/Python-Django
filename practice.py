#Add Two Numbers
# a=10
# b=20
# sum=a+b
# print("sum=",sum)

#Even odd 
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


#Find the largest of two numbers

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))

# if a>b:
#     print("Largest is:",a)
# else:
#     print("Largest is:",b)

# sum of first 10 natural numbers

# total = 0
# for i in range(1, 11):
#     total += i

# print("Sum =", total)

# Factorial of a number

# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num+1):
#     fact *= i

# print("Factorial =", fact)

# calculate simple interest

# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# si = (p * r * t) / 100
# print("Simple Interest =", si)


# find area of a circle
# radius = float(input("Enter radius: "))
# area = 3.14 * radius * radius
# print("Area of circle =", area)

# check if a character is vowel or not

# ch=input("Enter a character:")
# if ch.lower() in "aeiou":
#     print("Vowel")
# else:
#     print("Not a vowel")

# reverse a string

# text = input("Enter a string:")
# rev = text[::-1]
# print("Reversed string=",rev)


# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")
# else:
#     print("Not Prime")

# remove duplicate elements from list

# nums = [1,2,2,3,4,4]
# unquie=list(set(nums))
# print(unquie)

# count words in a sentence

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Word count =", len(words))

# Generate random password 

# import random
# import string 

# password = ""
# for i in range(8):
#     password+=random.choice(string.ascii_letters+string.digits)
# print("Password:",password)

# addition of two matrix

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]

print(result)
