class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for i in strs: # for each word in the list
          count=[0]*26 #makes the count 

          for j in i:
            count[ord(j)-ord("a")]+=1

          res[tuple(count)].append(i)
        return list(res.values())