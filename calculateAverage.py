def calculate_average(num_list):
    """
    This function takes a list of numbers as input and returns the average of those numbers.
    """
    if len(num_list) == 0:
        return None
    else:
        sum = 0
        for num in num_list:
            sum += num
        return sum / len(num_list)
