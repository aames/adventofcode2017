import unittest
import itertools

def evenly_divisible(a, b):
    """
    Check if two integers are evenly divisible values or not
    """
    if (a%b is 0) or (b%a is 0):
        return True
    return False

def find_divisible_values(values):
    """
    Given a list of integers, find the evenly divisible pair
    return them as a tuple: min, max
    """
    for value in values:
        if evenly_divisible(value[0],value[1]):
            if value[0] < value[1]:
                return value[0], value[1]
            else:
                return value[1], value[0]
    return False

def calc_row(values):
    """
    For a list of values, find each combination of 2 values,
    then find the result of the evenly divisible values
    e.g. 9, 3 = 3 because 9/3=3
    """
    values_for_checking = []
    # Use itertools to find every combination of 2 elements
    for subset in itertools.combinations(values, 2):
        values_for_checking.append([subset[0],subset[1]])
    minimum, maximum = find_divisible_values(values_for_checking)
    return maximum/minimum

def main(input):
    checksum=0
    for i in range(0,len(input)):
        checksum=checksum + calc_row(input[i])
    return checksum

def input():
    input_as_rows_ints = []
    f = open('day02part01.input', 'r+')
    input_as_rows = f.readlines()
    f.close()
    for i in range(0,len(input_as_rows)):
        input_as_rows_ints.append([int(x) for x in input_as_rows[i].split('\t')])
    return input_as_rows_ints

class TestChecksum(unittest.TestCase):
    """
    We have only one sample test case given;
    """
    def test_checksum(self):
        self.assertEqual(main([[5,9,2,8], [9,4,7,3], [3,8,6,5]]), 9)

if __name__ == '__main__':
    """
    Run the application with the input string. Also run the test.
    """
    print main(input())
    unittest.main()
