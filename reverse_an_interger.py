# Write a program to reverse an integer in Python.

def reversed_interger(number):
    # check if the number is negative 
    is_negative = False 

    if number<0:
        is_negative = True 
        number = abs(number)
    
    # convert  number to string and reverse the st12345ring and again convert it into interger 

    reversed_string = str(number)[::-1]
    reversed_num = int(reversed_string)

    if is_negative:
        reversed_num = -reversed_num 
    
    return reversed_num 


number = int(input())

result = reversed_interger(number) 

print(result) 


