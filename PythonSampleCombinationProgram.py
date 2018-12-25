# -*- coding: utf-8 -*-

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Prime numbers (Numbers - lower and upper limits)")
print("6.Fibonacci (Number = term)")
print("7.Factorial")
choice = input("Enter choice(1/2/3/4/5/6/7):")

num1 = int(input("Enter number: "))
if int(choice) < 6:
 num2 = int(input("Enter another number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
     for num in range(num1,num2 + 1):
      if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
            print(num)

elif choice == '6':
      n1 = 0
      n2 = 1
      count = 0
      if num1 <= 0:
       print("Please enter a positive integer")
      elif num1 == 1:
       print("Fibonacci sequence upto",num1,":")
       print(n1)
      else:
       print("Fibonacci sequence upto",num1,":")
       while count < num1:
           print(n1,end=' , ')
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1   
elif choice == '7':
 factorial = 1
 if num1 < 0:
   print("Sorry, factorial does not exist for negative numbers")
 elif num == 0:
   print("The factorial of 0 is 1")
 else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)           
else:
   print("Invalid input")     
    