# Palindromic Roman numerals

A (brute force) answer to the question: how many Roman numerals are palindromic?

A lot is known about decimal palindromic numbers.
By contrast, as far as we know,
even though Roman numerals have been around for a long time,
nobody had determined how many of them are.
The answer is 6,950, at least for one specific notation.
Further discussion, including on different answers for different notations,
can be found in an accompanying paper (to be published).

## The approach

The solution relies on two components:
+ a function that converts integers to Roman numerals
+ a function that checks if a given Roman numeral is palindromic

We chose a particular representation for Roman numerals for which
there are 3,999,999,999 possible numerals.
Since there are a finite number of Roman numerals, all we have to do is
to list all possible ones, and check which of them are palindromic.

The functionality of converting an integer to a Roman numeral
is based on jambonrose's
[roman-numerals](https://github.com/jambonrose/roman-numerals) library.
It does not support the notation we adopted, so we rewrote the function.

## Running the code

The code was written in Python 3.7 but should
work in previous Python 3 versions as well.
There are no dependencies.

To see a sample, running `$ python roman.py` prints a list of palindromic Roman numerals to stdout.
