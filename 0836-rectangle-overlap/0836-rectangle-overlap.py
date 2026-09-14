class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_left_x = rec1[0]
        rec1_bottom_y = rec1[1]
        rec1_right_x = rec1[2]
        rec1_top_y = rec1[3]

        rec2_left_x = rec2[0]
        rec2_bottom_y = rec2[1]
        rec2_right_x = rec2[2]
        rec2_top_y = rec2[3]

        return not (rec2_right_x <= rec1_left_x or 
rec2_left_x >= rec1_right_x or 
rec1_top_y <= rec2_bottom_y or 
rec1_bottom_y >= rec2_top_y)