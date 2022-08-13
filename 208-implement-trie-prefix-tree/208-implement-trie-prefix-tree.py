class treeNode:
    def __init__(self):
        self.isWord=False
        self.children=dict()
class Trie:

    def __init__(self):
        self.tre=treeNode()

    def insert(self, word: str) -> None:
        x=self.tre
        for i in word:
            if i not in x.children:
                x.children[i]=treeNode()
            x=x.children[i]
        x.isWord=True    
                
                

    def search(self, word: str) -> bool:
        x=self.tre
        for i in word:
            
            if i not in x.children:
                return False
            x=x.children[i]
      
        return x.isWord   

    def startsWith(self, prefix: str) -> bool:
        x=self.tre
        for i in prefix:
          
            if i not in x.children:
                return False
            x=x.children[i]
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)