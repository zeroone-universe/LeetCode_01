class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_para = []
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split():
            if word not in banned:
                new_para.append(word)
                
        counter = collections.Counter(new_para)
        return counter.most_common()[0][0]