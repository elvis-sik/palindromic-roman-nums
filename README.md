# Palindromic Roman numerals

> [!NOTE]
> **Historical project.** This 2019 exploration is archived and no longer
> maintained.

A brute-force answer to the question: how many Roman numerals are palindromic?
For the notation implemented here, the answer is **6,950**.

## Approach

The program combines:

- a function that converts integers to Roman numerals; and
- a function that tests whether a numeral is a palindrome.

The chosen representation contains 3,999,999,999 possible numerals, so the
program enumerates that finite space and checks each representation. The
conversion logic began from jambonrose’s
[roman-numerals](https://github.com/jambonrose/roman-numerals) library and was
adapted for the notation used in this experiment.

## Running the code

The code was written for Python 3.7 and has no third-party dependencies:

```bash
python roman.py
```

That command prints a sample of palindromic Roman numerals to standard output.
