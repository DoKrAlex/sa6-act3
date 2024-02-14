def find_maximum(numbers, comparison_func):
    """
    Find the maximum number in a list using a provided lambda function for comparison.

    Parameters:
        numbers (list): List of numbers.
        comparison_func (function): Lambda function to compare two numbers.

    Returns:
        int: Maximum number in the list.
    """
    if not numbers:
        raise ValueError("List must not be empty")

    # Initialize maximum with the first element of the list
    maximum = numbers[0]

    # Iterate over the list
    for num in numbers[1:]:
        # Use the provided lambda function to compare two numbers and update the maximum
        if comparison_func(num, maximum) > 0:
            maximum = num

    return maximum

# Example usage:
if __name__ == "__main__":
    # List of numbers
    numbers = [5, 8, 3, 12, 7, 9]

    # Lambda function for comparison (returns the greater of two numbers)
    comparison_lambda = lambda x, y: x - y

    # Find the maximum number in the list using the provided lambda function
    max_number = find_maximum(numbers, comparison_lambda)

    # Print the result
    print("Maximum number in the list:", max_number)
