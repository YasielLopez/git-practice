def max_value(numbers_1):
    """ This function returns the largest number
        in the list.
    """
    max = numbers_1[0]
    for num in numbers_1:
        if num > max:
            max = num
    return max


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
