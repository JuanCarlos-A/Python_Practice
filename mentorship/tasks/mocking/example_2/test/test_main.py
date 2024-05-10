import unittest
from unittest.mock import Mock

class TestExample(unittest.TestCase):

    json = Mock()


    json.loads(s='{"k" : "v"}')

    json.loads.assert_called()
    json.loads.assert_called_once()
    json.loads.assert_called_with(s='{"k" : "v"}')
    json.loads.assert_called_once_with(s='{"k" : "v"}')

    json.loads('{"k" : "v"}')

    json.loads.assert_called_with('{"k" : "v"}')
    # json.loads.assert_not_called()