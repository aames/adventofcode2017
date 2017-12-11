import unittest

def calc_row(values):
    return max(values)-min(values)

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
        self.assertEqual(main([[5,1,9,5],[7,5,3],[2,4,6,8]]), 18)

if __name__ == '__main__':
    """
    Run the application with the input string. Also run the test.
    """
    print main(input())
    unittest.main()
