class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=[]
        l1=len(word1)
        l2=len(word2)
        
        i,j=0,0
        while i<l1 and j<l2:
            s.append(word1[i])
            s.append(word2[j])
            i+=1
            j+=1
        s.extend(word1[i:])
        s.extend(word2[j:])
        return "".join(s)
