# Write a program in Python to check whether an integer is Armstrong number or not. 


# An Armstrong number  is a number that is the sum of its own digits each raised to the power of the number of digits. 
# In other words, an n-digit number is an Armstrong number if the sum of its digits, each raised to the power of n, 
# is equal to the original number.

def is_armstrong_number(num):
    # converts the number to string and find the number of digits in it 
    num_str = str(num)
    num_digits = len(num_str)

    # calculate the sum of the digits which raised to the power of its digits 
    armstrong_sum = 0 
    for i in num_str:
        power = int(i)**num_digits  
        armstrong_sum += power 
    # check wheather the sum is equal to original number
    return armstrong_sum == num 

def main():
    num = int(input()) 
    result = is_armstrong_number(num)
    print(result)

main()