import csv

from roman import create_list_of_palindromes, remove_bars


def read_test_data():
    with open('./test_data/below_5_million.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        return [(roman, int(decimal)) for (roman, decimal) in reader]

def generate_data():
    palindrome_tuples = create_list_of_palindromes(starting_from=1, up_to=5_000_000)
    return [(remove_bars(roman), decimal) for (roman, decimal) in palindrome_tuples]

def read_data():
    palindromes_list = []

    with open('palindromes.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for roman, decimal_str in reader:
            without_bars = remove_bars(roman)
            decimal = int(decimal_str)
            palindromes_list.append((without_bars, decimal))

    return palindromes_list

def compare_up_to_5_millions(generated_data_source=read_data):
    computed_data = generated_data_source()
    computed_data = set(computed_data)
    test_data = read_test_data()
    test_data = set(test_data)
    return {'in test, not computed': test_data - computed_data,
            'computed, not in test': computed_data - test_data}
