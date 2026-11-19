class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash1 = {}
        hash2 = {}
        for ss in s:
            if ss not in hash1:
                hash1[ss]=1
            else:
                hash1[ss]+=1
        for tt in t:
            if tt not in hash2:
                hash2[tt]=1
            else:
                hash2[tt]+=1
        print(hash1)
        print(hash2)
        for k in hash1.keys():
            if k not in hash2:
                return False
            else:
                if hash1[k]!=hash2[k]:
                    print(k)
                    print(f"{hash1[k]} {hash2[k]}")
                    return False
        
        return True
