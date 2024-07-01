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
