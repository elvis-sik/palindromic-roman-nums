# Palindromic Roman numerals

A (brute force) answer to the question: how many Roman numerals are palindromic?

We know a lot about decimal palindromic numbers.
By contrast, as far as we know,
even though Roman numerals have been around for a long time,
nobody had determined how many of them are.
The answer is 6,950, at least for one specific notation.
An accompanying paper will be published.

## The approach

The solution relies on two components:
+ a function that converts integers to Roman numerals
+ a function that checks if a given Roman numeral is palindromic

We chose a particular representation for Roman numerals for which
there are 3,999,999,999 possible numerals.
Since there are a finite number of Roman numerals, all we have to do is
to list all possible Roman numerals, and check which ones are palindromic.

The functionality of converting an integer to a Roman numeral
is based on jambonrose's
[roman-numerals](https://github.com/jambonrose/roman-numerals) library.
Since it does not support the notation we adopted, we had to adapt it.

## Running the code

The code was written in Python 3.7 but should
work in previous Python 3 versions as well.
There are no dependencies.
