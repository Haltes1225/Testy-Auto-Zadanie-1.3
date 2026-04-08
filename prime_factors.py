from sympy import *

def prime_factors(number):
    
    if isprime(number):
        result = [number]
        return result