class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log_list=[]
        letter_log_list=[]
        for log in logs:
            if log.split()[1].isdigit():
                digit_log_list.append(log)
            else :
                letter_log_list.append(log)
                
        letter_log_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        ans=letter_log_list+digit_log_list
        return ans
        