class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
        def ans(char):
            if char == "R":
                return "Radiant"
            else:
                return "Dire"

        senate = list(senate)
        senate_tf = []
        
        for senator in senate:
            senate_tf.append([senator, True])
        while True:
            for idx, senator in enumerate(senate):
                if senate_tf[idx][1] == True:
                    if senator == "R":
                        target = "D"
                    else:
                        target = "R"

                    if idx + 1 < len(senate) and [target, True] in senate_tf[idx+1:]:
                        idx_ch = senate_tf[idx+1:].index([target, True])
                        senate_ch = senate_tf[idx+1:]
                        senate_ch[idx_ch] = [target,False]
                        
                        senate_tf = senate_tf[:idx+1] + senate_ch

                    elif idx!=0 and [target, True] in senate_tf:
                        idx_ch = senate_tf.index([target, True])
                        senate_tf[idx_ch] = [target,False]

                    else:
                        return ans(senator)
                    
