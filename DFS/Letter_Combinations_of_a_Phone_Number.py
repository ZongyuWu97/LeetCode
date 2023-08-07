class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def generate(existing, digits):
            if not digits:
                return existing
            ans = []
            for arr in existing:
                for ch in mapping[digits[0]]:
                    ans.append(arr + ch)
            return generate(ans, digits[1:])
        
        return generate([''], digits)