class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        a=int(event1[0][:2])*60+int(event1[0][3:])
        b=int(event1[1][:2])*60+int(event1[1][3:])
        c=int(event2[0][:2])*60+int(event2[0][3:])
        d=int(event2[1][:2])*60+int(event2[1][3:])
        if b<c or d<a:
            return False
        return True