import sys
from typing import List, str
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Convert start and end times of events to minutes since midnight
        start_time1 = int(event1[0][:2]) * 60 + int(event1[0][3:])
        end_time1 = int(event1[1][:2]) * 60 + int(event1[1][3:])
        start_time2 = int(event2[0][:2]) * 60 + int(event2[0][3:])
        end_time2 = int(event2[1][:2]) * 60 + int(event2[1][3:])

        # Check for overlap
        if (start_time1 >= start_time2 and start_time1 <= end_time2) or (start_time2 >= start_time1 and start_time2 <= end_time1):
            return True
        if (end_time1 >= start_time2 and end_time1 <= end_time2) or (end_time2 >= start_time1 and end_time2 <= end_time1):
            return True
        return False
