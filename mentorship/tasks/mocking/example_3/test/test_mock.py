import unittest
from unittest.mock import Mock

class TestMocking(unittest.TestCase):

    def test_mock(self):
        json = Mock()

        json.loads('{"key": "value"}')

        print(json.loads.call_count)
        print(json.loads.call_args)
        print(json.loads.call_args_list)


if __name__ == '__main__':
    unittest.main()