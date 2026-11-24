import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.replace(" ", "")
        formatted = cleaned.lower()
        filtered = re.sub(r'[^a-z0-9]', '', formatted)
        if filtered == filtered[::-1]:
            return True
        else:
            return False
    

        

            
        