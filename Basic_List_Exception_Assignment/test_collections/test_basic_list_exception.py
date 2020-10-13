import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as basic_list_exception


class MyTestCase(unittest.TestCase):
 def test_make_list(self):
   with patch('fun_with_collections.basic_list_exception.get_input', return_value='9'):
    def test_make_list(self, input):
        self.assertEqual(basic_list_exception.make_list(input), [6, 89, -9])


if __name__ == '__main__':
    unittest.main()
