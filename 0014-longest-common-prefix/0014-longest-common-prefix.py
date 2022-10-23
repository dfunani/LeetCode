class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for letter in strs[0]:
            temp = []
            for word in strs[1:]:
                if word.startswith(res + letter):
                    temp.append(letter)
            if len(temp) == len(strs[1:]):
                res += letter
            else:
                return res
        return res