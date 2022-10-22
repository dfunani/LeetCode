class Solution:
    def romanToInt(self, s: str) -> int:
        
        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D" :500,
            "M": 1000,
        }
        r = 0
        for i,c in enumerate(s):
            try:
                r += (-conversion[c]) if  (c == 'I' and s[i + 1] in ["V", "X"]) or (c == 'X' and s[i + 1] in ["L", "C"]) or (c == 'C' and s[i + 1] in ["D", "M"]) else conversion[c]
            except:
                r += conversion[c]
        return r
        