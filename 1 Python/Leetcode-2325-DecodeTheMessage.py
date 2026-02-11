import string as s
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decoder = " " # we initiate with a blank space so that indexing stays sane
        for i in range(len(key)):
            letter = key[i]
            if letter not in decoder and letter!=" ":
                decoder+=letter
        letters = " " + s.ascii_lowercase #we initiate with blank space at start
        output = ""
        for l in message:
            output += letters[decoder.index(l)]

        return output
