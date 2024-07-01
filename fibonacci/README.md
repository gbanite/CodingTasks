# CodingTasks

# Fibonacci Sequence

## Description
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This coding task generates the first `n` numbers of the Fibonacci sequence.

Learning this aspect of coding is important because it introduces the concept of sequences and series, and helps in understanding recursion and iterative approaches in problem-solving.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
No specific installation is required. Ensure you have Python installed.

## Usage
To run the Fibonacci program, use the following command:
```bash
python fibonacci.py

## Credits

### Task 2: Fibonacci Sequence

**File:** `fibonacci\fibonacci.py`
```python
"""
Fibonacci Sequence: Generates the first n numbers in the Fibonacci sequence.
"""

def fibonacci(n):
    """
    Generates the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(fibonacci(n))

