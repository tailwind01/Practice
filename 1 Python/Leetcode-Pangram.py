class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        pangramCtr = 1
        for l in alphabet:
            if l in sentence:
                continue
            else:
                pangramCtr = 0
                break
        return bool(pangramCtr)
