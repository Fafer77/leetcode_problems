from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        y_lower_bound = float("inf")
        y_upper_bound = float("-inf")
        for x, y, l in squares:
            total_area += l ** 2
            y_lower_bound = min(y_lower_bound, y)
            y_upper_bound = max(y_upper_bound, y + l)
        
        above_area = total_area
        below_area = 0

        while y_upper_bound - y_lower_bound > 1e-5:
            y_mid = (y_upper_bound + y_lower_bound) / 2
            below_area = self.calculate_field_under_y(squares, y_mid)
            above_area = total_area - below_area

            if above_area > below_area:
                y_lower_bound = y_mid
            else:
                y_upper_bound = y_mid
        
        return y_upper_bound


    def calculate_field_under_y(self, squares, threshold):
        under_area = 0
        for x, y, l in squares:
            if y + l <= threshold:
                under_area += l ** 2
            elif y < threshold < y + l:
                fraction = threshold - y
                under_area += fraction * l
        
        return under_area
