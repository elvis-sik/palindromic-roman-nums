import roman


def read_test_data():
    """Read data in test_data.csv."""
    filename = './data/test_data.csv'
    return roman.read_pairs_from_csv(filename, skip_first=True)


def read_missing_in_test_data():
    """Read data in missing_in_test.csv."""
    filename = './data/missing_in_test.csv'
    list_of_missing_palindromes = roman.read_pairs_from_csv(filename,
                                                            skip_first=True)
    return set(list_of_missing_palindromes)


def known_wrong_palindromes_in_test_data():
    return {
        ('XXXDXXX', 30800),
        ('MCDM', 1_151_000),
        ('IXCCXI', 92_011),
        ('LXIXL', 61_040),
        ('LXIIXL', 62_040),
        ('LXIIIXL', 63_040),
        ('IVLXIXLVI', 4_061_046),
        ('IVLXIIXLVI', 4_062_046),
        ('IVLXIIIXLVI', 4_063_046),
    }


def generate_data_for_testing():
    "Generate data up to 5,000,000 for testing purposes"
    palindrome_tuples = roman.create_list_of_palindromes(starting_from=1,
                                                         up_to=5_000_000)
    return [(roman.remove_bars(roman_number), decimal)
            for (roman_number, decimal) in palindrome_tuples]


def compare_up_to_5_million(generated_data_source=generate_data_for_testing):
    """Compare manually compiled list with algorithm's predictions."""
    computed_data = generated_data_source()
    computed_data = set(computed_data)

    test_data = read_test_data()
    test_data = set(test_data)

    return {
        'in test, not computed': test_data - computed_data,
        'computed, not in test': computed_data - test_data
    }


def test_converting_a_few_random_numbers():
    assert roman.convert_to_numeral(3) == 'III'
    assert roman.convert_to_numeral(245) == 'CCXLV'
    assert roman.convert_to_numeral(7892) == '[VII]DCCCXCII'
    assert roman.convert_to_numeral(
        3_999_999_999) == '[[MMM]][[CMXCIX]][CMXCIX]CMXCIX'


def test_palindromes_up_to_5_million():
    comparison_dict = compare_up_to_5_million()

    predicted_missing_in_computed = comparison_dict['in test, not computed']
    predicted_missing_in_test = comparison_dict['computed, not in test']

    correct_missing_in_test = read_missing_in_test_data()
    correct_missing_in_computed = known_wrong_palindromes_in_test_data()

    assert predicted_missing_in_computed == correct_missing_in_computed
    assert predicted_missing_in_test == correct_missing_in_test
