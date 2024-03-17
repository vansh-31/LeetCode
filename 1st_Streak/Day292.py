# Problem : Backspace String Compare
# Problem Statement : Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sp, tp = len(s) - 1, len(t) - 1
        s_back = t_back = 0
        while sp >= 0 or tp >= 0:
            while sp >= 0 and (s[sp] == '#' or s_back > 0):
                if s[sp] == '#':
                    s_back += 1
                else:
                    s_back -= 1
                sp -= 1
            while tp >= 0 and (t[tp] == '#' or t_back > 0):
                if t[tp] == '#':
                    t_back += 1
                else:
                    t_back -= 1
                tp -= 1
            if sp == tp == -1:
                return True
            if (sp == -1 or tp == -1) and sp != tp:
                return False
            if s[sp] != t[tp]:
                return False
            sp -= 1
            tp -= 1
        return sp == tp