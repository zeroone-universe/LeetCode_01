class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        para = paragraph.split()
        
        
        words = [
            word for word in re.sub("[^\w]"," ", paragraph).lower().split() if word not in banned
        ]
        
        count = collections.Counter(words)
        return count.most_common(1)[0][0]