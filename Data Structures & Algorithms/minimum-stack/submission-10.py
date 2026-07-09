class MinStack:

    def __init__(self):
        self.st = []
        self.stMin = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.stMin and self.stMin[-1] > val:
            self.stMin.append(val)
        elif self.stMin:
            self.stMin.append(self.stMin[-1])
        else:
            self.stMin.append(val)
        
        return
            

    def pop(self) -> None:
        self.st.pop()
        self.stMin.pop()

        return

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.stMin[-1]
