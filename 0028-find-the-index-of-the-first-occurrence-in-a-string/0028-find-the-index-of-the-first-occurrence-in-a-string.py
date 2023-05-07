class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for idx in range(len(haystack) - len(needle)+1):
            if haystack[idx] == needle[0]:
                for n_idx in range(len(needle)):
                    if haystack[idx+n_idx] != needle[n_idx]:
                        break
                    if n_idx == len(needle) - 1:
                        return idx
        return -1