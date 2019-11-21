import csv

from roman import create_list_of_palindromes, remove_bars


def read_numbers_from_csv(file='./test_data.csv', skip_first=True):
    """Read numbers from file in format ROMAN;DECIMAL"""
    with open(file) as csvfile:
        if skip_first:
            csvfile.readline()

        reader = csv.reader(csvfile, delimiter=';')
        for roman, decimal_str in reader:
            without_bars = remove_bars(roman)
            decimal = int(decimal_str)
            palindromes_list.append((without_bars, decimal))
        return palindromes_list


def generate_data_for_testing():
    palindrome_tuples = create_list_of_palindromes(starting_from=1,
                                                   up_to=5_000_000)
    return [(remove_bars(roman), decimal)
            for (roman, decimal) in palindrome_tuples]


def compare_up_to_5_millions(generated_data_source=generate_data_for_testing):
    """Compare manually compiled list with algorithm's predictions."""
    computed_data = generated_data_source()
    computed_data = set(computed_data)

    test_data = read_test_data()
    test_data = set(test_data)

    return {
        'in test, not computed': test_data - computed_data,
        'computed, not in test': computed_data - test_data
    }
