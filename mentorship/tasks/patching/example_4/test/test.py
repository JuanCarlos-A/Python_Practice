import my_calendar
from unittest.mock import patch

with patch('my_calendar.is_weekday'):
    my_calendar.is_weekday()


# from my_calendar import is_weekday
# from unittest.mock import patch
# with patch('my_calendar.is_weekday'):
#     is_weekday()



# from my_calendar import is_weekday
# from unittest.mock import patch
# with patch('__main__.is_weekday'):
#     is_weekday()
