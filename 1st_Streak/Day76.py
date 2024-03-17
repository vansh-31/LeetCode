# Problem : Implement Trie (Prefix Tree)
# Problem Statement : A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
class Trie:

    def __init__(self):
        self.isTerminal = False
        self.arr = [None for x in range(26)]
        

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isTerminal = True
            return
        def insertUtils():
            if self.arr[ ord(word[0]) - 97 ] == None:
                self.arr[ ord(word[0]) - 97 ] = Trie()
            self.arr[ ord(word[0]) - 97 ].insert(word[1:])
        insertUtils()


    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.isTerminal

        def searchUtils():
            if self.arr[ ord(word[0]) - 97 ] == None:
                return False
            return self.arr[ ord(word[0]) - 97 ].search(word[1:])
        return searchUtils()

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        def startswithUtils():
            if self.arr[ ord(prefix[0]) - 97 ] == None:
                return False
            return self.arr[ ord(prefix[0]) - 97 ].startsWith(prefix[1:])
        return startswithUtils()


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)