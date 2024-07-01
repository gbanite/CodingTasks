# FizzBuzz

## Description
FizzBuzz is a simple coding task that prints numbers from 1 to `n`, but for multiples of 3, it prints "Fizz" instead of the number, and for multiples of 5, it prints "Buzz". For numbers which are multiples of both 3 and 5, it prints "FizzBuzz".

Learning this aspect of coding is important because it teaches fundamental concepts such as loops, conditionals, and modulus operations, which are commonly used in many programming tasks.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
No specific installation is required. Ensure you have Python installed.

## Usage
To run the FizzBuzz program, use the following command:
```bash
python fizzbuzz.py

## Credits
Author: Olisaemeka Ezeako

"""
FizzBuzz: Prints numbers from 1 to n, replacing multiples of 3 with "Fizz",
multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
"""

def fizzbuzz(n):
    """
    Prints the FizzBuzz sequence up to the number n.

    Args:
        n (int): The upper limit of the sequence.
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(100)
