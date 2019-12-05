"""Converting decimal numbers to Roman numerals and checking for palindromes."""

import csv
import re

UPPER_LIMIT = 3_999_999_999
UPPER_LIMIT_STR = "[[MMM]][[CMXCIX]][CMXCIX]CMXCIX"

ROMAN_NUMERAL_TABLE = [{
    "bars": 2,
    "symbols": [(1_000_000_000, "M")],
}, {
    "bars":
    2,
    "symbols": [
        (900_000_000, "CM"),
        (500_000_000, "D"),
        (400_000_000, "CD"),
        (100_000_000, "C"),
        (90_000_000, "XC"),
        (50_000_000, "L"),
        (40_000_000, "XL"),
        (10_000_000, "X"),
        (9_000_000, "IX"),
        (8_000_000, "VIII"),
        (7_000_000, "VII"),
        (6_000_000, "VI"),
        (5_000_000, "V"),
        (4_000_000, "IV"),
    ],
}, {
    "bars": 1,
    "symbols": [
        (1_000_000, "M"),
    ],
}, {
    "bars":
    1,
    "symbols": [
        (900_000, "CM"),
        (500_000, "D"),
        (400_000, "CD"),
        (100_000, "C"),
        (90_000, "XC"),
        (50_000, "L"),
        (40_000, "XL"),
        (10_000, "X"),
        (9_000, "IX"),
        (8_000, "VIII"),
        (7_000, "VII"),
        (6_000, "VI"),
        (5_000, "V"),
        (4_000, "IV"),
    ],
}, {
    "bars":
    0,
    "symbols": [
        (1_000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
}]


def convert_to_numeral(decimal_integer: int, roman_format="brackets"):
    """Convert decimal to Roman numeral.

    roman_format is a str containing either 'brackets' or 'latex'
    The default option, 'brackets', converts 3,000,000,000 to [[MMM]] and
    3,000,000 to [MMM].

    'latex' outputs a LaTeX formula for the numeral.
    """
    def barfunction_latex(prefix: str,
                          unbarred_string: str,
                          num_of_bars: int,
                          separator_size: int = 2):
        """Return a LaTeX-renderable representation of overline bars."""
        bars_before = (r"\overline{" * num_of_bars) + r"\text{"
        bars_after = r"}" + ("}" * num_of_bars)

        if prefix:
            separation = f"\\hspace{{{separator_size}pt}}"
        else:
            separation = ""

        return prefix + separation + bars_before + unbarred_string + bars_after

    def barfunction_brackets(prefix: str, unbarred_string: str,
                             num_of_bars: int):
        """Represent bars as (possibly nested) square brackets.

        For example, 3,000,000,000 is converted to [[MMM]].
        """
        bars_before = ("[" * num_of_bars)
        bars_after = ("]" * num_of_bars)
        return prefix + bars_before + unbarred_string + bars_after

    def latex_surround_with_dollars(string):
        """Surround LaTeX math expression with dollar signs."""
        return "$" + string + "$"

    def list_occurring_roman_symbols(roman_symbols, integer_value):
        """List symbols that occur in Roman representation of number.

        + roman_symbols is [(int, str)], a list of tuples, each of which
          representing one Roman symbol and its corresponding integer value.
          For example, (3, 'III').
        + integer_value is the value to be converted.

        Return: remainder, list_of_occurring_symbols
        + remainder: what remains from the number, which was too small to
          represent with the provided symbols
        + list_of_occurring_symbols: a list of the symbols present in the Roman
          representation of the number.
        """
        remainder = integer_value
        list_of_occurring_symbols = []

        for integer_value, str_roman_symbol in roman_symbols:
            repetitions, remainder = divmod(remainder, integer_value)
            list_of_occurring_symbols.append(str_roman_symbol * repetitions)

        return remainder, list_of_occurring_symbols

    def apply_barfunction(list_of_occurring_symbols, barfunction,
                          numeral_string, num_of_bars):
        """Build up Roman numeral representation applying barfunction.

        The barfunction is only applied if list_of_occurring_symbols is not
        empty, otherwise the original numeral_string is returned untouched.
        """
        unbarred_string = "".join(list_of_occurring_symbols)
        if unbarred_string:
            numeral_string = barfunction(numeral_string, unbarred_string,
                                         num_of_bars)
        return numeral_string

    if roman_format == 'latex':
        barfunction = barfunction_latex
    elif roman_format == 'brackets':
        barfunction = barfunction_brackets
    else:
        raise ValueError('roman_format should be either "latex" or "brackets"')

    remainder = decimal_integer
    numeral_string = ""

    for symbolset in ROMAN_NUMERAL_TABLE:
        num_of_bars = symbolset["bars"]
        symbols = symbolset["symbols"]

        remainder, list_of_occurring_symbols = list_occurring_roman_symbols(
            symbols, remainder)

        numeral_string = apply_barfunction(list_of_occurring_symbols,
                                           barfunction, numeral_string,
                                           num_of_bars)

    if roman_format == 'latex':
        return latex_surround_with_dollars(numeral_string)
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
    """Return argument without square brackets ('[' and ']')."""
    return re.sub(r"[\[\]]", "", string)


def is_palindrome(num):
    """Check if a string is palindromic."""
    try:
        numeral_str = convert_to_numeral(num)
    except TypeError:
        numeral_str = num
    without_bars = remove_bars(numeral_str)
    left, right = split_str(without_bars)
    return left == reverse_str(right)


def create_list_of_palindromes(starting_from=1,
                               up_to=UPPER_LIMIT,
                               save=False,
                               verbose=False,
                               filename="./data/palindromes.csv",
                               mode="a+"):
    """Create list of palindromes.

    If save is True, the list is written to a file. The filename and mode in
    which it is opened are given by the arguments. Otherwise, a list is
    returned.

    If verbose is True, every 1000-th number is printed to the screen.

    The other arguments the numbers in which the list starts and ends.
    """
    def create_list_on_loop(command):
        """Higher-order function that generates a list of palindromes.

        This is used mainly to avoid having to repeat the same loop twice.
        """
        for decimal in range(starting_from, up_to + 1):
            if decimal % 1000 == 0 and verbose:
                print(f"\r{decimal:,}", end="")

            roman = convert_to_numeral(decimal)
            if is_palindrome(roman):
                command(roman, decimal)

    if verbose:
        print()

    if save:
        with open(filename, mode) as palindromes:

            def write_numeral_to_file(roman, decimal):
                """Write numerals to file.

                Used as a command to higher-order function create_list_on_loop.
                """
                palindromes.write(f"{roman};{decimal}\n")

            create_list_on_loop(write_numeral_to_file)
    else:
        palindromes = []

        def append_numeral_to_list(roman, decimal):
            """Append numerals to list.

            Used as a command to higher-order function create_list_on_loop.
            """
            palindromes.append((roman, decimal))

        create_list_on_loop(append_numeral_to_list)

    if verbose:
        print()

    if not save:
        return palindromes


def read_pairs_from_csv(filename, skip_first=False):
    """Read numbers from file in format ROMAN;DECIMAL.

    This will return a list of (roman_numeral: string, decimal: int) tuples.
    The Roman numerals will have square brackets removed.
    """
    with open(filename) as csvfile:
        if skip_first:
            csvfile.readline()

        reader = csv.reader(csvfile, delimiter=";")
        palindromes_list = []
        for roman, decimal_str in reader:
            without_bars = remove_bars(roman)
            decimal = int(decimal_str)
            palindromes_list.append((without_bars, decimal))
        return palindromes_list


def create_palindromes_tex(input_file="./data/palindromes.csv",
                           output_file="./latex_list/Palindromes.tex"):
    """Read palindromes.csv and saves Palindromes.tex

    Converts pre-compiled palindromes list, saved in square-brackets format and
    decimals, to a TeX file.
    """
    def read_decimals_from_csv(filename):
        """Return only decimals from palindromes CSV file.

        See read_pairs_from_csv.
        """
        pairs_list = read_pairs_from_csv(filename)
        decimals_list = [decimal for (roman, decimal) in pairs_list]
        return decimals_list

    def convert_bunch_of_decimals(decimals_list):
        """Pair decimals with their LaTeX-formatted Roman counterparts.

        decimals_list is a list of ints
        Return: list of (roman: string, decimal: int) pairs
        """
        pairs = []
        for dec in decimals_list:
            roman = convert_to_numeral(dec, roman_format='latex')
            pairs.append((roman, dec))
        return pairs

    def save_to_file(string):
        """Overwites output_file with string."""
        with open(output_file, "w") as file:
            file.write(string)

    def format_single_number(roman, decimal):
        """Format single line of LaTeX table."""
        INDENTATION = "  "
        return INDENTATION + roman + " & " + str(decimal) + r" \\"

    FIRST_LINE = r"\begin{longtable}{ p{.60\textwidth}  p{.20\textwidth} }"
    NEWLINE = "\n"
    FINAL_LINE = r"\end{longtable}"

    palindrome_decimals = read_decimals_from_csv(input_file)
    roman_dec_pairs = convert_bunch_of_decimals(palindrome_decimals)

    numbers_lines = [format_single_number(*pair) for pair in roman_dec_pairs]

    latex_string = (FIRST_LINE + NEWLINE + "\n".join(numbers_lines) + NEWLINE +
                    FINAL_LINE)
    save_to_file(latex_string)
