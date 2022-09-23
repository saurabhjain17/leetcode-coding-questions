class WordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()
        
    def addWord(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = WordNode()
                node = node.children[w]
        node.isEnd = True
                
    def search(self, word):
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0]=='.':
                for n in node.children.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))
        return False