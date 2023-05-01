class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        return (sum(salary)-salary[0]-salary[-1])/float(len(salary)-2)
        