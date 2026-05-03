
# n=int(t)
# print(n)
# name="Alice"
# age=26
# score=90.5
# message1="My name is" + name +",I am" + str(age) +" years old,and my score is " + str(score)
# print(message1)
# name="ram"
# age=25
# print("my name is {},and i am {} years old." .format(name,age))
# studenprint("hello python")
# x,y=(10,20)
# print("sum",x+y)
# print("product",x*y)
# print("modulus",x%y)
# print("division",x/y)
# print("difference",x-y)
# print("exponent",x**y)
# print(pow(x,y))
# r="60"
# v=int(r)
# print(v)
# t=79.6
# name="ram"
# age=37
# message_template="hello, i am {s_name}. i am {a} years old"
# m = message_template.format(s_name=name,a=age)
# print(m)
# text="python world"
# print(text.capitalize())
# print(text.upper())
# print(text.lower())
# print(text.swapcase())
# print(len(text))
# print(text.startswith("th"))
# print(text.endswith("ld"))
# print(text.count("y"))
# print(text.find("o"))
# print(text.split("world"))
# students=["neeru","ami","anji"]
# print(students)
# students[2]="meera"
# print(students)
# students.append("ram")
# print(students)
# students.insert(2,"meera")
# print(students)
# fruits=["apple","banana","cherry","date","elderberry","fig","grape"]
# print(fruits[:3])
# print(fruits[2:6])
# print(fruits[-3:])
# print(fruits[::2])
# print(fruits[::-1])
# numbers=[5,2,9,1,2]
# numbers.sort()
# print(numbers)
# def area_circle(radius):
#     area=3.14*radius*radius
#     return radius,area
# r,area=area_circle
# print("Area:",a)
# print("Radius:",r)
# add=lambda num: num + 10
# print("sum :",add(5))
# multiply=lambda a, b: a * b
# print("product:",multiply(3,5))
# area=lambda r:r*r * 3.14
# print("area:",area(4))
# isEven=lambda num: "True" if num % 2==0 else "False"
# print(isEven(2))
# print(isEven(4))
n1=5
n2=6
# operator=input("enter a operator")
# if operator=='+':
#     print("add",n1+n2)
# elif operator=='-':
#     print("difference",n1-n2)
# elif operator=='*':
#     print("product",n1*n2)
# else:
#    print("invalid operator")
# orders=[100,2000,300,4000]
# for order in orders :
#     tax = order * 10/100
#     print(f"orderd amount:{order},Tax:{tax}")
# count=0
# while count<=20:
#     count=count+2
#     print(count)
# class student:
#     def __init__(self,roll_no,name,course):
#        self.roll_no= roll_no
#        self.name= name
#        self.course= course
#     def display_info(self):
#        print(f"roll no:{self.roll_no}")
#        print(f"name:{self.name}")
#        print(f"course:{self.course}")
# s1=student(1,"anjima","cs")
# s1.display_info()
# s2=student(2,"amri","cs")
# s2.display_info()
# s3=student(3,"neeru","cs")
# s3.display_info()
# s4=student(4,"anjana","cs")
# s4.display_info()
# s5=student(5,"sandra","cs")
# s5.display_info()
# class product:
#     def __init__(self,id,title,price):
#         self.id=id
#         self.title=title
#         self.price=price
# class Electronicproduct(product):
#     def __init__(self,id,title,price,warranty,manufacture):
#         super(). __init__(id,title,price)
#         self.warranty=warranty
#         self.manufacture=manufacture
# prod1=Electronicproduct(1,"oppo",2000,4,"oppo")
# prod1.price=18000
# print(prod1.price)
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=amt
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
    def display(self):
        print(self.name,self.balance)
acc=BankAccount("Anji",2000)
acc.deposit(500)
acc.withdraw(200)
acc.display()
