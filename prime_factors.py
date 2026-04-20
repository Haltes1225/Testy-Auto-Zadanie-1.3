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
    elif number % 2 == 0 or number % 3 == 0:
        if number == 2 or number == 3:
            return True
        else:
            return False
    else:
        #since number is non divisible by 2 or 3, it is not divisible by 6, so it is not of the form 6k, where k is natural
        #since it is not divisible by 2, it is not of the form 6k + 2 or 6k + 4
        #since it is not divisible by 3, it is not of the form 6k + 3
        #this leaves 6k + 1 and 6k + 5 (or 6k - 1)
        if number % 6 == 1 or number % 6 == 5:
            #we can also only look for factors among numbers 6k +- 1
            k = 1
            while (6*k-1)*(6*k-1) <= number:
                if number % (6*k - 1)  == 0 or number % (6*k + 1) == 0:
                    return False
                k += 1
            return True
        else:
            return False

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

        

   
