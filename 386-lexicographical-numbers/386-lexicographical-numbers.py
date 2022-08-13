class Trie:
    def __init__(self):
        self.child=dict()
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        dic={str(i):i for i in range(0,10)}
        root=Trie()
        for i in range(1,n+1):
            string=str(i)
            nod=root
            for j in string:
                if j not in nod.child:
                    nod.child[j]=Trie()
                nod=nod.child[j]
        out=[]
        def rec(nod,tem):
            
            if len(nod.child)==0:
                # print("ok")
                # out.append(tem)
                return
            for i in range(0,10):
                if str(i) in nod.child:
                    # print("Ok")
                    out.append(tem*10+i)
                    rec(nod.child[str(i)],tem*10+i)
        rec(root,0)
        # print(root.child)
        return out