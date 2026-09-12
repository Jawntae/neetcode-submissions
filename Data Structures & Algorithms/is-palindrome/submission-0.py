class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        f = 0
        b = -1

        # make everything lowercase, and remove non-alphanumeric values
        cleanTxt = re.sub(r'[^a-zA-Z0-9]', '', s)
        txt = cleanTxt.lower()
        n = len(txt)

        while f < n:
            # if not palindrome, false
            if txt[f] is not txt[b]: return False
            f += 1
            b -= 1
        return True



    # Allows:
    # A-Z
    # a-z
    # 0-9