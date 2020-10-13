"""
Program: basic_list.py
Author: Ihsanullah Anwary
Last date modified: 10/07/2020
This program asks the user for three numbers and makes a list and get_input get one input return it.
"""
_list = []


def make_list(_input):
    """ It makes the list"""
    for i in range(3):  # loop
        try:

            _input = int(input("Please enter a number"))  # asks for input.
        except ValueError:  # exception validation.
            print("Enter a number")
        _list.append(_input)  # store the list.


def get_input(_list):
    """ It gets one input and return it"""
    return ('return_value=' + str(_list[1]))  # string output.


if __name__ == '__main__':
    make_list([3, 5, 6])
    get_input(_list)