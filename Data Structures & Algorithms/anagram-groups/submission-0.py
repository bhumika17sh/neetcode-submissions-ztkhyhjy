class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrammap[key].append(word)

        return list(anagrammap.values())