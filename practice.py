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

# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# result = [[0, 0], [0, 0]]

# for i in range(2):
#     for j in range(2):
#         result[i][j] = A[i][j] + B[i][j]

# print(result)


# merge two lists and sort

# a=[1,4,6]
# b=[2,3,5]
# merged = a+b
# merged.sort()
# print(merged)

# a=['c','b','a']
# b=['d','f','e']

# merged = a+b 
# merged.sort()
# print(merged)

# Exception handling example

# try:
#     a=int(input("Enter number:"))
#     b=int(input("Enter number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# simple class and object

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)

# s = Student("Rahul", 85)
# s.display()

# simple class and object

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# p = Person("Shashank", 20)
# p.display()


# student class (marks & result)

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks=marks

#     def result(self):
#         if self.marks>=40:
#             print(self.name,"Pass")
#         else:
#             print(self.name,"Fail")

# s1 = Student("Amit",75)
# s1.result()


# library system

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def show_books(self):
#         for book in self.books:
#             print(book)

# lib = Library()
# lib.add_book("Python")
# lib.add_book("Data Structures")
# lib.show_books()

# static method

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(5, 3))

# rectangle class

# class rectangle:
#     def __init__(self,l,b):
#         self.l= l
#         self.b= b

#     def area(self):
#         print("Area=",self.l*self.b)

#     def perimeter(self):
#         print("Perimeter=",2*(self.l+self.b))

# r=rectangle(5,3)
# r.area()
# r.perimeter()

# simple cal using class

# class calculator:
#     def add(self,a,b):
#         print("Add=",a+b)
#     def sub(self,a,b):
#         print("Sub=",a-b)
    
# c = calculator()
# c.add(10,5)
# c.sub(10,5)

# simple timer counter 

# class Timer:
#     def __init__(self):
#         self.time = 0

#     def tick(self):
#         self.time += 1

#     def show(self):
#         print("Time:", self.time)

# t = Timer()
# t.tick()
# t.tick()
# t.show()

# simple message class

# class Message:
#     def show(self):
#         print("Welcome to python OOP")

# m=Message()
# m.show()

# Temperature converter

# class Temperature:
#     def c_to_f(self, c):
#         print("F =", (c * 9/5) + 32)

# t = Temperature()
# t.c_to_f(30)

# Grade system

# class Grade:
#     def calculate(self, marks):
#         if marks >= 75:
#             print("Distinction")
#         elif marks >= 50:
#             print("Pass")
#         else:
#             print("Fail")

# g = Grade()
# g.calculate(48)

# simple shopping cart

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def show_items(self):
#         print(self.items)

# c = Cart()
# c.add_item("Pen")
# c.add_item("Book")
# c.show_items()

# counter using class variable

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1

# obj1 = Counter()
# obj2 = Counter()

# print("Total objects:", Counter.count)

# prime number

# n=int(input("Enter Number:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("Not prime")
#             break
#         else:
#             print("Prime")

# power of a number

# a=int(input("Base:"))
# b=int(input("Exponent:"))
# print(a**b)






