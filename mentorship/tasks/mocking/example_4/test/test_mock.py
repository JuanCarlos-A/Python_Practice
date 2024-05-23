from unittest.mock import Mock
import datetime


def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() < 5)


tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()

datetime.datetime.today.return_value = tuesday

assert is_weekday()

datetime.datetime.today.return_value = saturday

assert is_weekday()


