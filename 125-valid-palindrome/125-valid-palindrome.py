class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list=collections.deque()
        
        for char in s:
            if char.isalnum() is True:
                s_list.append(char.lower())
            
        while len(s_list)>1:
            if s_list.popleft() !=s_list.pop():
                return False
        return True