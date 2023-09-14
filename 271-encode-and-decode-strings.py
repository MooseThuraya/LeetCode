class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = []
        for word in strs:
            wordLen = str(len(word))
            letters = list(word)
            output = output + [wordLen] + ["#"] + letters
        return "".join(output)


        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            #[3#TEA]
            lenWord = int(s[i:j])
            j+=1
            word = s[j:j+lenWord]
            res.append(word)
            i = j+lenWord
        return res
        "5#Hello5#World"
        # i=7
        # j=8
        # len = 5
        # word = s[7:7]
        # ["Hello"]