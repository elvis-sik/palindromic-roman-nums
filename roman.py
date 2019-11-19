""""""

import re

UPPER_LIMIT = 3_999_999_999
UPPER_LIMIT_STR = '[[MMM]][[CMXCIX]][CMXCIX]CMXCIX'

ROMAN_NUMERAL_TABLE = [{
    "bars": 2,
    "symbols": [(1_000_000_000, 'M')],
}, {
    "bars":
    2,
    "symbols": [
        (900_000_000, 'CM'),
        (500_000_000, 'D'),
        (400_000_000, 'CD'),
        (100_000_000, 'C'),
        (90_000_000, 'XC'),
        (50_000_000, 'L'),
        (40_000_000, 'XL'),
        (10_000_000, 'X'),
        (9_000_000, 'IX'),
        (8_000_000, 'VIII'),
        (7_000_000, 'VII'),
        (6_000_000, 'VI'),
        (5_000_000, 'V'),
        (4_000_000, 'IV'),
    ],
}, {
    "bars": 1,
    "symbols": [
        (1_000_000, 'M'),
    ],
}, {
    "bars":
    1,
    "symbols": [
        (900_000, 'CM'),
        (500_000, 'D'),
        (400_000, 'CD'),
        (100_000, 'C'),
        (90_000, 'XC'),
        (50_000, 'L'),
        (40_000, 'XL'),
        (10_000, 'X'),
        (9_000, 'IX'),
        (8_000, 'VIII'),
        (7_000, 'VII'),
        (6_000, 'VI'),
        (5_000, 'V'),
        (4_000, 'IV'),
    ],
}, {
    "bars":
    0,
    "symbols": [
        (1_000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
}]


def convert_to_numeral(decimal_integer):
    remainder = decimal_integer

    numeral_string = ""

    for symbolset in ROMAN_NUMERAL_TABLE:
        bars = symbolset['bars']
        symbols = symbolset['symbols']
        return_list = []

        for integer, numeral in symbols:
            repetitions, remainder = divmod(remainder, integer)
            return_list.append(numeral * repetitions)

        unbarred_string = ''.join(return_list)
        if unbarred_string:
            barred_string = ('[' * bars) + unbarred_string + (']' * bars)
            numeral_string = numeral_string + barred_string

    return numeral_string


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


def split_str(numeral_str):
    """Split a string in two halves of equal size."""
    left = numeral_str[:len(numeral_str) // 2]

    if is_even(len(numeral_str)):
        right = numeral_str[len(numeral_str) // 2:]
    else:
        right = numeral_str[len(numeral_str) // 2 + 1:]
    return left, right


def reverse_str(numeral_str):
    """Reverses the order of a string."""
    return numeral_str[::-1]


def remove_bars(string):
    return re.sub(r'[\[\]]', '', string)


def is_palindrome(num):
    """Check if a string is palindromic."""
    try:
        numeral_str = convert_to_numeral(num)
    except TypeError:
        numeral_str = num
    without_bars = remove_bars(numeral_str)
    left, right = split_str(without_bars)
    return left == reverse_str(right)


def create_list_of_palindromes(starting_from=1, up_to=UPPER_LIMIT, save=True, verbose=False):
    # taking about 19s for 1 million numbers
    # for 20 million numbers, should take about 66 mins

    def save_list_to_file(filename, lst):
        with open(filename, 'w') as file:
            for roman, decimal in lst:
                file.write(f"{roman};{decimal}\n")

    palindromic_nums = []

    for decimal in range(starting_from, up_to + 1):
        if decimal % 1000 == 0 and verbose:
            print(f'\r{decimal:,}', end='')

        roman = convert_to_numeral(decimal)
        if is_palindrome(roman):
            palindromic_nums.append((roman, decimal))

    if save:
        filename = f'palindromes_{starting_from}_{up_to}.csv'
        save_list_to_file(filename, palindromic_nums)

    if verbose:
        print()

    return palindromic_nums


def list_palindromes_on_disk(starting_from=1, up_to=UPPER_LIMIT, filename='palindromes.csv', verbose=True):
    if verbose:
        print()

    with open(filename, 'a+') as palindromes:
        for decimal in range(starting_from, up_to + 1):
            if decimal % 1000 == 0 and verbose:
                print(f'\r{decimal:,}', end='')

            roman = convert_to_numeral(decimal)
            if is_palindrome(roman):
                palindromes.write(f'{roman};{decimal}\n')

    if verbose:
        print()