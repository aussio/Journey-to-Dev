import unittest

def leap_frog(array):
    '''Determine if the input list can be sucessfully leap-frogged.

    For each element in the list, you can traverse forward in the list *up to* value of the current element in the list.
    You are sucessful if you are able to reach the very last item in the list in this way.

    Examples:
        Given the input array [2, 0, 0]:
        Since the first element is 2, you can traverse forward to the last element in the list. This would return True

    Given the input array [1, 0, 0]:
        From the first element, you could move forward a single element.
        The value of the second element is 0, and it is not the last item in the list.
        Since there are no other alternate "routes", this would return False.

    Args:
        array: a non-empty list of integers.

    Return:
        bool: True if the end can be reached, False otherwise.
    '''
    num_possible_moves = array.pop(0)

    if len(array) == 0:
        return True
    elif len(array) <= num_possible_moves:
        return True

    for next_move in get_next_moves(array, num_possible_moves):
        if leap_frog(next_move):
            return True

    return False
      
def get_next_moves(array, num_possible_moves):
    '''Helper function for leap_frog to get all possible next moves'''
    next_moves = []

    for index in range(num_possible_moves):
        if array[index] != 0:
            next_moves.append(array[index:])

    return next_moves
  
class TestLeapFrog(unittest.TestCase):
  
    def test_leap_frog_should_return_true(self):
        '''
        Test to confirm that we return True when an array can be successfully traversed.
        '''
        self.assertTrue(leap_frog([0]))
        self.assertTrue(leap_frog([1, 0]))
        self.assertTrue(leap_frog([2, 0]))
        self.assertTrue(leap_frog([2, 0, 1, 0]))
        self.assertTrue(leap_frog([2, 2, 2, 0, 1, 1]))
        self.assertTrue(leap_frog([6, 0, 1, 0]))

    def test_leap_frog_should_return_false(self):
        '''
        Test to confirm that we return False when an array is not traversable.
        '''
        self.assertFalse(leap_frog([0, 1]))
        self.assertFalse(leap_frog([1, 0, 0]))
        self.assertFalse(leap_frog([2, 0, 0, 1]))
        self.assertFalse(leap_frog([2, 2, 2, 0, 1, 0, 1]))
        self.assertFalse(leap_frog([0, 6, 1, 0]))

if __name__ == '__main__':
  unittest.main(verbosity=2)
