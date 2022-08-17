class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lis=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x=ord("a")
        dic={chr(i+x):lis[i] for i in range(26)}
        seti=set()
        for word in words:
            op=""
            for wo in word:
                op+=dic[wo]
            seti.add(op)
        return len(seti)    