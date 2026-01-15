def is_prime(n):
    count=0
    for i in range(1, int(math.sqrt(n)) + 1):
        if(count>=1):
            return False
        if(n%i == 0):
            count+=1
    return True
    
    

n=int(input("enter your number : "))


if(is_prime(n)):
     print(f"your number {n} is prime")
else:
    print(f"your number {n} is notprime")