# Problem 41:
#     Pandigital Prime
#
# Description:
#     We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
#
#     For example, 2143 is a 4-digit pandigital and is also prime.
#
#     What is the largest n-digit pandigital prime that exists?

from math import floor, sqrt


def is_pandigital(n: int) -> bool:
    """
    Returns True iff `n` is pandigital

    Args:
        n (int): Natural number

    Returns:
         (bool): True iff `n` is pandigital

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # Can't be pandigital if more than 9 digits
    if n >= 10 ** 10:
        return False

    s = str(n)
    digits = set(map(int, list(s)))
    return digits == set(range(1, len(s)+1))


def main() -> int:
    """
    Returns the largest pandigital prime

    Returns:
        (int): Largest pandigital prime
    """
    # Idea:
    #     Only pandigitals of these lengths can be prime.
    #     Consider each possible pandigital size:
    #       1 digit     => Digits = {1}         => Only candidate is 1, which is not prime  => EXCLUDE
    #       2 digits    => Digits = {12}        => All candidates are multiples of 3        => EXCLUDE
    #       3 digits    => Digits = {123}       => All candidates are multiples of 3        => EXCLUDE
    #       4 digits    => Digits = {1234}
    #       5 digits    => Digits = {12345}     => All candidates are multiples of 3        => EXCLUDE
    #       6 digits    => Digits = {123456}    => All candidates are multiples of 3        => EXCLUDE
    #       7 digits    => Digits = {1234567}
    #       8 digits    => Digits = {12345678}  => All candidates are multiples of 3        => EXCLUDE
    #       9 digits    => Digits = {123456789} => All candidates are multiples of 3        => EXCLUDE
    possible_digits = {4, 7}
    n = int(''.join(map(str, range(max(possible_digits), 0, -1)))) + 1

    # Use Sieve of Eratosthenes to get all primes below `n`
    # Also check if each is pandigital
    sieve = []
    pan_p = 0
    for x in range(2, n):
        # Use already found primes to check if `x` prime
        x_is_prime = True
        x_mid = floor(sqrt(x)) + 1  # Only need to check divisibility up to here
        i = 0
        while i < len(sieve) and sieve[i] < x_mid:
            p = sieve[i]
            if x % p == 0:
                x_is_prime = False
                break
            i += 1
        if x_is_prime:
            sieve.append(x)
            if len(str(x)) in possible_digits and is_pandigital(x):
                pan_p = x
    return pan_p


if __name__ == '__main__':
    largest_pandigital_prime = main()
    print('Largest pandigital prime:')
    print('  {}'.format(largest_pandigital_prime))
