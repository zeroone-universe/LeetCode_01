class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        def func(x):
            return x.split()[1:], x.split()[0]
        
        letter_logs.sort(key = func)
        
        return letter_logs + digit_logs