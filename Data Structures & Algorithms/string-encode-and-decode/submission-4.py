class Solution:

    def encode(self, strs: List[str]) -> str:
        s='_123'.join(strs)
        return s if strs else "None"

    def decode(self, s: str) -> List[str]:
        strs=s.split('_123')
        return strs if s!="None" else []
