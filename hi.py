#print("just be", "a friend")
# message = input("Enter smth")
# print(message)
# x = ("kidding")
# y = 5

# print(type(x))
# print(type(y))
# x = int(input("Enter Number 1"))
# y = int(input("Enter Number 2"))
# print("Answer" + str(x + y))
# print("Answer", (x + y))
# print("yes","i know")
# print("yes" + "i know")
# x = int(input("Enter First Number"))
# y = int(input("Enter Second Number"))
# print("Your answer is",(x+y))
# print("Your answer is" + str(x+y))
# x = "hello"
# print(type(x))
# y = 6
# print(type(y))
# age = int(input("Enter your age"))
# if age > 18:
# 	print("Drink beer")

# else:
# 	print("Drink cola")
# result = 16
# guess = int(input("Guess your number between (10,20)"))
# if guess > 16:
# 	print("Wrong Guess,Try smaller")

# elif guess< 16:
# 	print("Wrong Guess,Try bigger")

# elif guess==16:
# 	print("Correct")
# guess = input("enyter your day 'rainy','windy','sunny' : ")
# if guess =="rainy":
# 	print("take a umberalla")
# elif guess =="windy":
# 	print("Liverpool ManU ko shone loc")
# elif guess =="sunny":
# 	print("sor nk hangout lyk")
# user = 'sai'
# psw = '4567'
# username = input("Username : ")
# password = input("Password : ")
# if username==user and password==psw:
# 	print("Hello, " + username)
# elif username==user and password!=psw:
# 	print("Wrogn Answer, nga trr")
# elif username!=user or password!=psw:
# 	print("Username or Psw error, Try again ")
# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))
# choice = input("+,-,*,/ : ")

# if choice=="+":
# 	answer = num1 + num2
# 	print("Answer is" + str(answer))
# elif choice=="-":
# 	answer = num1 - num2
# 	print("Answer is" + str(answer))
# elif choice=="*":
# 	answer = num1 * num2
# 	print("Answer is" + str(answer))
# elif choice=="/":
# 	answer= num1 / num2
# 	print("Answer is" + str(answer))
#
import random
choice = int(input("Choose between Head1 and Tail2  :"))
coin = random.randint(1,2)
if coin==1:
	print('Head')
if coin==2:
	print('Tail')
if choice==2 and coin==1:
	print("You lose")
elif choice==2 and coin==2:
	print("You win")
elif choice==1 and coin==1:
	print("You win")
elif choice==2 and coin==1:
	print("You lose")



 	

















