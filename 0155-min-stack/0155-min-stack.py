class MinStack:

    def __init__(self):
        self.stack = []
        self.min  = []        

    def push(self, value: int) -> None:
        if not self.stack :
            self.stack.append(value)
            self.min.append(value)
        else:
            if self.min[-1] < value:
                self.min.append(self.min[-1])
                self.stack.append(value)
            else:
                self.stack.append(value)
                self.min.append(value)
        # print(self.stack, self.min)

        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()