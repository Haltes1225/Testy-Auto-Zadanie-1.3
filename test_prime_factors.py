def test_import_prime_factors():
    try:
        from prime_factors import prime_factors
        assert callable(prime_factors), "prime_factors not callable"
    except ImportError as error:
        assert False, error

from prime_factors import prime_factors

if __name__ == '__main__':
    for test in (
        test_import_prime_factors,
    ):  #➜ 4
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)