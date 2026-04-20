from functools import wraps
import math

def validate_number(function):

    @wraps(function)
    def wrapper(number):
        type_number = type(number)  
        if not type_number is int:
            raise TypeError(f"number must be int type, is {type_number}")
    
        if not number > 0:
            raise ValueError("number must be an integer greater than 0")

        if number == 1:
            return None
        
        return function(number)
    return wrapper

@validate_number
def is_prime(number):

    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        if number % 2 == 0 or number % 3 == 0:
            return False
        else:
            m = 2
            while m < number:
                if number % m == 0:
                    return False
                m += 1
            return True

@validate_number
def prime_factors(number):
    
    if is_prime(number):
        result = [number]
        return result
    else:
        result = []
        number_remainder = number
        for i in range(math.floor(math.sqrt(number)+1)):
            j=i+1
            if is_prime(j):
                while number_remainder % j == 0:
                    result.append(j)
                    number_remainder = number_remainder//j
                if j > number_remainder:
                    break
        if number_remainder > 1:
            result.append(number_remainder)
        return result

        

   
