# Problem : Design Add and Search Words Data Structure
# Problem Statement : Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dic[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.dic[len(word)]

        for v in self.dic[len(word)]:
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
                
        return False