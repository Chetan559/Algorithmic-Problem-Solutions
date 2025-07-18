class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
        # self.min_ele = 2**31 - 1

    def push(self, val: int) -> None:
        self.stk.append(val)
        # self.min_ele = min(self.min_ele, val)
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)

    def pop(self) -> None:
        val = self.stk.pop()
        if val == self.min_stk[-1]:
            self.min_stk.pop()
        # if len(self.stk) != 0:
            # self.min_ele = min(self.stk)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()