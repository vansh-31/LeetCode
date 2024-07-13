# Problem : Robot Collisions
# Problem Statement : There are n 1-indexed robots, each having a position on a line, health, and movement direction.
# You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.
# All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
# If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.
# Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
# Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
# Note: The positions may be unsorted.
class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        stack = []
        for i in sorted(range(len(positions)), key=lambda i: positions[i]):
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[stack[-1]] < healths[i]:
                    healths[i] -= 1
                    healths[stack.pop()] = 0
                if stack:
                    if healths[stack[-1]] == healths[i]:
                        healths[stack.pop()] = 0
                    else:
                        healths[stack[-1]] -= 1
                    healths[i] = 0
        return [h for h in healths if h]
