"""
Program: basic_list.py
Author: Ihsanullah Anwary
Last date modified: 10/07/2020
This program asks the user for three numbers and makes a list and get_input get one input return it.
validate the input and try exception.
"""
_list = []

list = []


def make_list(user_input):
    """ create the list"""
    for i in range(3):




        user_input = int(input("Please, Enter a number"))

        if user_input> 50:
            print('Invalid number')
        elif user_input< 0:
            print("No negative number")
        else:
            raise ValueError('Wrong input') # try exception .
        list.append(user_input)
    print("Value of list", list)
    return list


def get_input(list):

    """ get the a value ot the list"""
    print('return_value=' + str(list[1]))
    return ('return_value=' + str(list[1]))


if __name__ == '__main__':
    make_list([3, 5, 6])
    get_input(list)
