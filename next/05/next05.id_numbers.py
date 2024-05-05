class IDIterator:
    def __init__(self, id_number):
        self.id_number = id_number

    def __iter__(self):
        if (self.id_number < 0 or self.id_number > 999999999): # check if id_number is valid
            raise StopIteration
        return self

    def __next__(self):
        self.id_number += 1
        while not check_id_valid(self.id_number): # check if id_number is valid
            self.id_number += 1
        return self.id_number


def id_generator(id_number):
    """
    Generates a sequence of valid ID numbers starting from the given id_number.

    Parameters:
    id_number (int): The starting ID number.

    Yields:
    int: The next valid ID number in the sequence.
    """
    while True:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number


def reduce_num(num):
    if num > 9: # if the number is greater than 9, reduce it by 9
        return num - 9
    return num


def check_id_valid(id_number):
    return sum(list(map(reduce_num, [int(str(id_number)[i]) * 2 for i in range(len(str(id_number))) if i % 2 != 0])) + [int(str(id_number)[i])
                                                                                                                        for i in range(len(str(id_number))) if i % 2 == 0]) % 10 == 0


def main():
    id = input("Enter ID number: ") # get the ID number from the user
    type_of_iter = input("Enter type of iterator (it/gen): ") # get the type of iterator from the user
    if type_of_iter == "it": # if the type of iterator is "it", use IDIterator
        iterator = IDIterator(int(id)) # create an instance of IDIterator
        for _ in range(10): # print the next 10 valid ID numbers
            print(next(iterator)) # get the next valid ID number
    elif type_of_iter == "gen": # if the type of iterator is "gen", use id_generator
        iterator = id_generator(int(id)) # create an instance of id_generator
        for _ in range(10): # print the next 10 valid ID numbers
            print(next(iterator)) # get the next valid ID number


if __name__ == '__main__':
    main()
