# Write a program in Python to check given number is prime or not. 

def is_prime(num):
    # check if the number is less than 2 

    if num<2:
        return False 
    
    # check for factors from 2 to the square root of number 
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False 
    # if no factors found the number is prime 
    return True 

def main():
    num = int(input())
    result = is_prime(num)
    
    if result:
        print(f"{num} is a prime Number")
    else:
        print(f"{num} is Not a prime Number")

main()