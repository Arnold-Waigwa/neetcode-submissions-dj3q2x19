class PrefixTree:

    def __init__(self):
        self.strings = []
        
    def insert(self, word: str) -> None:
        #insert at end of list
        self.strings.append(word)


    def search(self, word: str) -> bool:
        for s in self.strings:
            if s == word:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for s in self.strings:
            if s.startswith(prefix):
                return True
        return False
        
        