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
    test_number = int(floor(prime_number_1 * prime_number_2))
    expected = [prime_number_1, prime_number_2]
    result = prime_factors(test_number)
    assert expected == result, f'Expected {expected}, got {result}'

def test_two_prime_factors_power_number_prime_factors():
    prime_number_1 = 3
    power_1 = 4
    prime_number_2 = 7
    power_2 = 2
    test_number = int(floor(pow(prime_number_1, power_1) * pow(prime_number_2, power_2)))
    expected = [prime_number_1 for x in range(power_1)] + [prime_number_2 for x in range(power_2)]
    result = prime_factors(test_number)
    assert expected == result, f'Expected {expected}, got {result}'

def test_three_prime_factors_power_number_prime_factors():
    prime_number_1 = 3
    power_1 = 4
    prime_number_2 = 7
    power_2 = 2
    prime_number_3 = 6037
    power_3 = 3
    test_number = int(floor(pow(prime_number_1, power_1) * pow(prime_number_2, power_2) * pow(prime_number_3, power_3)))
    expected = [prime_number_1 for x in range(power_1)] + [prime_number_2 for x in range(power_2)] + [prime_number_3 for x in range(power_3)]
    result = prime_factors(test_number)
    assert expected == result, f'Expected {expected}, got {result}'

def test_large_prime_number_prime_factors():
    prime_number = 19134702400093278081449423917 #source: https://oeis.org/A005478
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_non_int_type_prime_factors():
    try:
        prime_factors([3])
        assert False, 'TypeError expected'
    except TypeError:
        pass

def test_zero_number_prime_factors():
    try:
        prime_factors(0)
        assert False, 'ValueError expected'
    except ValueError:
        pass

def test_one_number_prime_factors():
    result = prime_factors(1)
    assert result == None, f'Expected None, got {result}'

def test_negative_number_prime_factors():
    try:
        prime_factors(-2)
        assert False, 'ValueError expected'
    except ValueError:
        pass

def test_none_prime_factors():
    try:
        prime_factors(None)
        assert False, 'TypeError expected'
    except TypeError:
        pass
def test_empty_prime_factors():
    try:
        prime_factors()
        assert False, 'TypeError expected'
    except TypeError:
        pass

from prime_factors import prime_factors

if __name__ == '__main__':
    for test in (
        test_import_prime_factors,
        test_prime_number_prime_factors,
        test_prime_power_number_prime_factors,
        test_semiprime_number_prime_factors,
        test_two_prime_factors_power_number_prime_factors,
        test_three_prime_factors_power_number_prime_factors,
        test_large_prime_number_prime_factors,
        test_non_int_type_prime_factors,
        test_zero_number_prime_factors,
        test_one_number_prime_factors,
        test_negative_number_prime_factors,
        test_none_prime_factors,
        test_empty_prime_factors
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)