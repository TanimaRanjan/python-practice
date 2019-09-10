class UncountableError(ValueError):
    def __init__(self, n):
        super().__init__(f'Invalid value for {n}, WRONG_VALUE. n must be greater than 0.')


def count_from_zero_to_n(n):
    if n < 0:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


val = input('Enter a integer : ')
count_from_zero_to_n(int(val))
