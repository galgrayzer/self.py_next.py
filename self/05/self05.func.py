def func(num1, num2) -> bool:
    """
    Check if the absolute difference between num1 and num2 is equal to 1.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        bool: True if the absolute difference is equal to 1, False otherwise.
    """
    if abs(num1 - num2) == 1:  # Check if the absolute difference between num1 and num2 is equal to 1.
        return True
    return False


def main():
    # Call the func function and print the result.
    print(func(1, 2))


if __name__ == '__main__':
    main()
