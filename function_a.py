def most_common_value(number_list):
    frequency_index = {}
    max_frequency = -1
    most_common_value = None

     for num in number_list:
        if num in frequency_index:
            frequency_index[num] += 1
        else:
            frequency_index[num] = 1


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
