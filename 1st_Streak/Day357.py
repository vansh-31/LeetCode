# Problem : Path Crossing
# Problem Statement : Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0,0)
        visited = {(0,0)}
        transition ={
            "N":(0,1),
            "S":(0,-1),
            "E":(1,0),
            "W":(-1,0)
        }
        for p in path:
            pos = (pos[0] + transition[p][0], pos[1] + transition[p][1])
            if pos in visited:
                return True
            visited.add(pos)
        return False