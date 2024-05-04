def shift_left(my_list: list):
    # shift the elements of the list to the left
    first_elem = my_list[0]  # store the first element
    for i in range(1, len(my_list)):  # shift the elements to the left
        my_list[i - 1] = my_list[i]
    my_list[-1] = first_elem  # set the last element to the first element
    return my_list  # return the shifted list


def main():
    print(shift_left([0, 1, 2]))
    print(shift_left(['monkey', 2.0, 1]))


if __name__ == '__main__':
    main()
