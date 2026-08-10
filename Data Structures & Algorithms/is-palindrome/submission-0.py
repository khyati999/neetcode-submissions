class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''
        for st in s:
            if st.isalnum():
                newStr+=st.lower()
        return newStr==newStr[::-1]