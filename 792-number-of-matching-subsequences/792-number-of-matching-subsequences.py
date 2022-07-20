class Solution:
     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
            dic={chr(ord("a")+i):[] for i in range(26)}
            counti=0
            for  word in words:
                dic[word[0]].append(word)
            for char in s:
                list_word=dic[char]
                dic[char]=[]
                for i in list_word:
                    if len(i)==1:
                        counti+=1
                    else:
                        dic[i[1]].append(i[1:])
            return counti   
        
#    ~~~Hello! Before I explain my solution, I would like to give credit to the post that inspired it. Here is a link with a description of the original algorithm.

# I begin by creating a default dictionary of 'list' objects. The main benefit of a default dictionary is that when you access an entry that does not yet exist, the entry is created automatically (in this case, the value for the entry is an empty list when it is created). I then create a 'count' variable to keep track of the number of words that are subsequences of the given string.

# The first thing I do with the dictionary is populate it with all the words in the list of words. The key for each entry is the first letter of the word. The value is the list of words that start with that letter. Using the example in the problem, the dictionary would look like the following:

# {'a': ['a', 'acd', 'ace'], 'b': ['bb']}

# The next step is to iterate through each character in the given string. For each character, I access the dictionary to retrieve the list of words that start with that character. I reset the value of the entry to an empty list and then iterate through the list of words I retrieved. If the word is only a single letter, then I conclude that we have successfully found a completed subsequence and increase our 'count' by one. Otherwise, I slice off the first character and add the sliced word back to the dictionary. This time, it is added to the entry for which the key is equal to the first letter of the sliced word.

# This process continues until we have iterated through all characters in the string. At the end, I return the count.~~~
    
    # def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    #     dic={chr(ord("a")+i):[] for i in range(26)}
    #     counti=0
    #     for  word in words:
    #         dic[word[0]].append(word)
    #     for char in s:
    #         list_word=dic[char]
    #         dic[char]=[]
    #         for i in list_word:
    #             if len(i)==1:
    #                 counti+=1
    #             else:
    #                 dic[i[1]].append(i[1:])
    #     return counti            
            
            