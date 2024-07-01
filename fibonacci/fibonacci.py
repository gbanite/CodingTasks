
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
