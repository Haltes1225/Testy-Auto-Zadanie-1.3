from sympy import *

def prime_factors(number):

    type_number = type(number)  
    if not type_number is int:
        raise TypeError(f"number must be int type, is {type_number}")
    
    if not number > 1:
        raise ValueError("number must be an integer greater than 1")
    
    if isprime(number):
        result = [number]
        return result
    else:
        result = []
        number_remainder = number
        for i in range(floor(sqrt(number)+1)):
            j=i+1
            if isprime(j):
                while number_remainder % j == 0:
                    result.append(j)
                    number_remainder = floor(number_remainder / j)
                if j > number_remainder:
                    break
        if number_remainder > 1:
            result.append(number_remainder)
        return result
        

   
