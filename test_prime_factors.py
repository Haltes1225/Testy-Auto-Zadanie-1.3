from sympy import *

def test_import_is_prime():
    try:
        from prime_factors import is_prime
        assert callable(is_prime), "prime_factors not callable"
    except ImportError as error:
        assert False, error

def test_is_prime_2():
    result = is_prime(2)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_3():
    result = is_prime(3)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_4():
    result = is_prime(4)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_9():
    result = is_prime(9)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6():
    result = is_prime(6)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_5():
    result = is_prime(3)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_25():
    result = is_prime(25)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_7():
    result = is_prime(7)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_49():
    result = is_prime(49)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_semiprime_number_is_prime():
    prime_number_1 = 3
    prime_number_2 = 17
    test_number = int(floor(prime_number_1 * prime_number_2))
    expected = False
    result = is_prime(test_number)
    assert expected == result, f'Expected {expected}, got {result}'

def test_is_prime_6k_1_prime():
    result = is_prime(613)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k_1_non_prime():
    result = is_prime(6*466222+1)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k_2():
    result = is_prime(6*345676788+2)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k_3():
    result = is_prime(6*9947889278785+3)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k_4():
    result = is_prime(6*40096883+4)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k_5_prime():
    result = is_prime(5039)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k_5_non_prime():
    result = is_prime(6*46622+5)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_is_prime_6k():
    result = is_prime(6*400968839884868989343443)
    expected = False
    assert result == expected, f'Expected {expected}, got {result}'

def test_big_prime_number_is_prime():
    prime_number = 479001599 #source: https://oeis.org/A088054
    result = is_prime(prime_number)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_very_big_prime_number_is_prime():
    prime_number = 63018038201 #source: https://oeis.org/A088165
    result = is_prime(prime_number)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_large_prime_number_is_prime():
    prime_number = 489133282872437279 #source: https://oeis.org/A088165
    result = is_prime(prime_number)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_very_very_large_prime_number_is_prime():
    prime_number = 19134702400093278081449423917 #source: https://oeis.org/A005478
    result = is_prime(prime_number)
    expected = True
    assert result == expected, f'Expected {expected}, got {result}'

def test_non_int_type_is_prime():
    try:
        is_prime([3])
        assert False, 'TypeError expected'
    except TypeError:
        pass

def test_is_prime_0():
    try:
        is_prime(0)
        assert False, 'ValueError expected'
    except ValueError:
        pass

def test_is_prime_1():
    result = is_prime(1)
    assert result == None, f'Expected None, got {result}'

def test_negative_number_is_prime():
    try:
        is_prime(-2)
        assert False, 'ValueError expected'
    except ValueError:
        pass

def test_none_is_prime():
    try:
        prime_factors(None)
        assert False, 'TypeError expected'
    except TypeError:
        pass

def test_empty_is_prime():
    try:
        is_prime()
        assert False, 'TypeError expected'
    except TypeError:
        pass

def test_import_prime_factors():
    try:
        from prime_factors import prime_factors
        assert callable(prime_factors), "prime_factors not callable"
    except ImportError as error:
        assert False, error

def test_prime_number_prime_factors_2():
    prime_number = 2
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_prime_number_prime_factors_3():
    prime_number = 3
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_prime_factors_4():
    number = 4
    result = prime_factors(number)
    expected = [2,2]
    assert result == [2,2], f'Expected {expected}, got {result}'

def test_prime_factors_9():
    number = 9
    result = prime_factors(number)
    expected = [3,3]
    assert result == expected, f'Expected {expected}, got {result}'

def test_prime_factors_6():
    number = 6
    result = prime_factors(number)
    expected = [2,3]    
    assert result == expected, f'Expected {expected}, got {result}'

def test_non_prime_non_divisible_by_2_or_3_prime_factors():
    number = 25
    result = prime_factors(number)
    expected = [5,5]
    assert result == expected, f'Expected {expected}, got {result}'

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

def test_big_prime_number_prime_factors():
    prime_number = 479001599 #source: https://oeis.org/A088054
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_very_big_prime_number_prime_factors():
    prime_number = 63018038201 #source: https://oeis.org/A088054
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_large_prime_number_prime_factors():
    prime_number = 489133282872437279 #source: https://oeis.org/A088165
    result = prime_factors(prime_number)
    assert result == [prime_number], f'Expected [{prime_number}], got {result}'

def test_very_very_large_prime_number_prime_factors():
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
from prime_factors import is_prime

if __name__ == '__main__':
    for test in (
        test_import_is_prime,
        test_is_prime_2,
        test_is_prime_3,
        test_is_prime_4,
        test_is_prime_9,
        test_is_prime_6,
        test_is_prime_5,
        test_is_prime_25,
        test_is_prime_7,
        test_is_prime_49,
        test_semiprime_number_is_prime,
        test_is_prime_6k,
        test_is_prime_6k_1_prime,
        test_is_prime_6k_1_non_prime,
        test_is_prime_6k_2,
        test_is_prime_6k_3,
        test_is_prime_6k_4,
        test_is_prime_6k_5_prime,
        test_is_prime_6k_1_non_prime,
        test_very_big_prime_number_is_prime,
        test_big_prime_number_is_prime,
        #test_large_prime_number_is_prime,
        #test_very_very_large_prime_number_is_prime,
        test_is_prime_0,
        test_is_prime_1,
        test_none_is_prime,
        test_empty_is_prime,
        test_negative_number_is_prime,
        test_import_prime_factors,
        test_prime_number_prime_factors_2,
        test_prime_number_prime_factors_3,
        test_prime_factors_4,
        test_prime_factors_9,
        test_prime_factors_6, 
        test_non_prime_non_divisible_by_2_or_3_prime_factors,
        test_prime_power_number_prime_factors,
        test_semiprime_number_prime_factors,
        test_two_prime_factors_power_number_prime_factors,
        test_three_prime_factors_power_number_prime_factors,
        test_big_prime_number_prime_factors,
        test_very_big_prime_number_prime_factors,
        #test_large_prime_number_prime_factors,
        #test_very_very_large_prime_number_prime_factors,
        test_non_int_type_prime_factors,
        test_zero_number_prime_factors,
        test_one_number_prime_factors,
        test_negative_number_prime_factors,
        test_none_prime_factors,
        test_empty_prime_factors
    ):
        """
        test_import_prime_factors,
        test_prime_number_prime_factors_2,
        test_prime_number_prime_factors_3,
        test_prime_factors_4,
        test_prime_factors_9,
        test_prime_factors_6, 
        test_non_prime_non_divisible_by_2_or_3_prime_factors,               
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
        """
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)