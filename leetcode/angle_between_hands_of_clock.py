# PROBLEM DESCRIPTION:
# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour 
# and the minute hand.
# 
# # EXAMPLE:
# INPUT:                                    OUTPUT:
# hour = 12, minutes = 30                   165
# 
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# hour = 3, minutes = 30                    75
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# hour = 3, minutes = 15                    7.5
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# hour = 4, minutes = 50                    155
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# hour = 12, minutes = 0                    0
# 
# CONSTRAINTS:
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.

# class Solution:
#     def angleClock(self, hour: int, minutes: int) -> float:
#         right_pie_hour = hour * 30 % 360
#         left_pie_hour = (12-hour) * 30 % 360
#         print(f'right hand pie: {right_pie_hour}, left hand pie: {left_pie_hour}') 
        
#         minute_hand_angle = minutes * 6
#         print("minute hand:", minute_hand_angle)
#         adjustment = (30 / 12) * (minutes / 5)
#         print('adjustment:', adjustment)
        
#         right_pie = abs(right_pie_hour - minute_hand_angle + adjustment)
#         left_pie = abs(left_pie_hour + minute_hand_angle) - adjustment)
#         print(f'right pie: {right_pie}, left hand pie: {left_pie}')
        
#         return min(right_pie, left_pie)

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_hand = minutes / 5
        hand_diff = hour - min_hand
        crossed = False

        if hand_diff < 0:
            hand_diff = abs(hand_diff)
            crossed = True

        angle = hand_diff * 30
        adjustment = (30 / 12) * min_hand

        angle = (angle-adjustment) if crossed else (angle+adjustment)

        return min(angle, 360-angle)