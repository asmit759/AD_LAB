import math
import random
# print("Welcome to AI Lab")
###################################################

# name=input("Student name: ")
# roll= int(input("Enter roll: "))
# branch = input("Enter  branch")

# print(name,roll,branch)
####################################################

# a= int(input("Enter a: "))
# b= int(input("Enter b: "))

# c=input("what do you want to perform: + - * /")

# match(c):
#     case("+"):
#         print(a+b)
#     case("-"):
#         print(a-b)
#     case("*"):
#         print(a*b)
#     case _:
#         print(a/b)

#####################################################

# cel= float(input("Enter temperature in celcius: "))
# far=(9/5)*cel + 32
# print(f"Your temp in farehnite = {far}")

######################################################

# a=int(input("enter a number"))
# if(a%2==0):
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

#######################################################

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))

# if(a>b and a>c):
#     print(a)
# elif(b>c):
#     print(b)
# else:
#     print(c)

########################################################

# n=int(input("enter a number"))
# sum=0
# for i in range (n):
#     sum+=i
# print(f"sum of {n} natural number is : {sum}")

##########################################################

# n=int(input("enter a number"))
# fact=1
# for i in range (1,n+1):
#     fact*=i
# print(fact)

###########################################################

# a=[]
# for i in range (5):
#     num = int(input(f"enter {i+1}th number"))
#     a.append(num)
# print(a)
# print(min(a))
# print(max(a))

############################################################
import math
def is_prime(n):
    count=0
    for i in range(1, int(math.sqrt(n)) + 1):
        if(count>1):
            return False
        if(n%i == 0):
            count+=1
    return True
    
    

n=int(input("enter your number : "))


if(is_prime(n)):
     print(f"your number {n} is prime")
else:
    print(f"your number {n} is notprime")

#################################################################

# choices = ["rock", "paper", "scissor"]
# pc = random.choice(choices)
# user = input("enter your choice : ").lower()

# print(f"Computer chose: {pc}")
# print(f"You chose: {user}")

# if pc == user:
#   print("draw")
# elif (user != "rock")  and \
#      (user != "paper") and \
#      (user != "scissor"):
#   print("invalid input")
# elif (pc == "rock" and user == "scissor") or \
#      (pc == "paper" and user == "rock") or \
#      (pc == "scissor" and user == "paper"):
#   print("Computer wins!")
# else:
#   print("You win!")