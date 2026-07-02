class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = []
        sizes = []
        for word in strs:
            sizes.append(len(word))
        for s in sizes:
            encoded_str.append(str(s))
            encoded_str.append(str("-"))
        encoded_str.append("!")
        encoded_str.extend(strs)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        size_str, response = s.split("!", 1)
        res = []
        i = 0
        sizes = [int(x) for x in size_str[:-1].split('-')]
        
        for size in sizes:
            res.append(response[i:i+size])
            i += size
        return res
        