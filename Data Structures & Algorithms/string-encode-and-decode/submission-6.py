class Solution:

    # broadcaster, String[] -> str
    # single str sent over network
    # reciever, str -> String[]

    #String[] -> str
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"
        encoded_str = "-|".join(strs)
        print(encoded_str)
        return encoded_str

    #str -> String[]
    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        encoded = s.split("-|")
        print(encoded)
        return encoded

    #[""-|] -> ""
    # init ideas

    # str in String[] and combine into on str with comma seperators
    # "hello,world,nice,to,meet,you" -> [hello, world, nice, to, meet, you] CSV like

    #if single elem, or empty str just send single elem as str
        # ["hello"] or [""] -> "hello" or ""
    # if empty String[] send single empty elem over
        # [] -> []
    # if comma in word: "we,ve" -> problem
    # use diff seperator -> | 

    # [hello, world, we,ve, arrived] -> "hello|world|we,ve|arrived"