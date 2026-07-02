class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            anagram = "".join(sorted(word))
            if anagram not in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(word)
        
        output = []
        for value in anagrams.values():
            output.append(value)

        return output