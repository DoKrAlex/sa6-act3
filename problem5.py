def raise_to_power(numbers, n):
    """
    Raise each number in the list to the power of n using a lambda function and map().

    Parameters:
        numbers (list): List of numbers.
        n (int): Constant value to raise the numbers to.

    Returns:
        list: List of numbers raised to the power of n.
    """
    # Use map() with a lambda function to raise each number to the power of n
    powered_numbers = list(map(lambda x: x ** n, numbers))
    return powered_numbers

# Example usage:
if __name__ == "__main__":
    # List of numbers
    numbers = [1, 2, 3, 4, 5]

    # Constant value
    n = 3

    # Raise each number in the list to the power of n
    powered_numbers = raise_to_power(numbers, n)

    # Print the result
    print(f"Numbers raised to the power of {n}:", powered_numbers)
