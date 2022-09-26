class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1>=bx2 or ax2<=bx1 or ay1>=by2 or by1>=ay2:
            p= 0
        else:
            p=(min(ax2,bx2)-max(ax1,bx1))*(min(ay2,by2)-max(ay1,by1))
        area=abs(ax2-ax1)*abs(ay2-ay1)+  abs(bx2-bx1)*abs(by2-by1) -p
        return area