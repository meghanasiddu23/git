def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first number.

    Parameters:
    a (int or float): The number to be subtracted from.
    b (int or float): The number to subtract.

    Returns:
    int or float: The result of the subtraction.
    """
    return a - b

if __name__ == "__main__":
    result_add = add(3, 5)
    print(f"The result of addition is: {result_add}")

    result_subtract = subtract(10, 2)
    print(f"The result of subtraction is: {result_subtract}")
