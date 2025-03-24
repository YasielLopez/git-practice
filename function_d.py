def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max = 0
    for number in numbers:
        if number > max:
            max = number
    return max


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
