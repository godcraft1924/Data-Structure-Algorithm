class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dicti = dict(knowledge)
        result = []
        current_key = []
        opening = False
        for i in s :
            if i == "(":
                opening = True
            elif i ==")":
                opening = False
                str_key = "".join(current_key)
                result.append(dicti.get(str_key, "?"))
                current_key = []
            elif opening :
                current_key.append(i)
            else:
                result.append(i)
        return "".join(result)