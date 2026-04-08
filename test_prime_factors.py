from sympy import *

def test_import_prime_factors():
    try:
        from prime_factors import prime_factors
        assert callable(prime_factors), "prime_factors not callable"
    except ImportError as error:
        assert False, error

def test_prime_number_prime_factors():
    prime_number = 3
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_prime_power_number_prime_factors():
    prime_number = 3
    power = 5
    test_number = pow(prime_number, power)
    expected = [prime_number for x in range(power)]
    result = prime_factors(test_number)
    assert expected == result, f'Expected {expected}, got {result}'

def test_semiprime_number_prime_factors():
    prime_number_1 = 3
    prime_number_2 = 17
    test_number = floor(prime_number_1 * prime_number_2)
    expected = [prime_number_1, prime_number_2]
    result = prime_factors(test_number)
    print(result)
    assert expected == result, f'Expected {expected}, got {result}'


from prime_factors import prime_factors

if __name__ == '__main__':
    for test in (
        test_import_prime_factors,
        test_prime_number_prime_factors,
        test_prime_power_number_prime_factors,
        test_semiprime_number_prime_factors
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)