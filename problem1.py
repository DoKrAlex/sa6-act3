# Function to compute the sum of digits using a lambda function
sum_of_digits = lambda num: sum(int(digit) for digit in str(num) if digit.isdigit())

# Test the function
if __name__ == "__main__":
    # Input number
    num = 12345
    
    # Compute sum of digits
    result = sum_of_digits(num)
    
    # Print result
    print(f"The sum of digits of {num} is: {result}")
