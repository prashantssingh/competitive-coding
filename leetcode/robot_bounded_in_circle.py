# PROBLEM DESCRIPTION:
# On an infinite plane, a robot initially stands at (0, 0) and faces north. 
# The robot can receive one of three instructions:
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
# 
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
# 
# EXAMPLES:
# INPUT:                                                    OUTPUT:
# "GGLLGG"                                                  true
# EXPLANATION: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# 
# INPUT:                                                    OUTPUT:
# "GG"                                                      false
# EXPLANATION: The robot moves north indefinitely.
# Example 3:
# 
# INPUT:                                                    OUTPUT:
# "GL"                                                      true
# EXPLANATION: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
# 
# NOTE:
# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
# 

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # after moving right, left, down, up, respectively
        direction = ((1,0), (0,-1), (-1,0), (0,1))

        x, y, i = 0, 0, 0

        for inst in instructions:
            if inst == "R":
                i = (i + 1) % 4
            elif inst == "L":
                i = (4 + i - 1) % 4
            else:
                x += direction[i][0]
                y += direction[i][1]
                
        return (x == 0 and y == 0) or i > 0