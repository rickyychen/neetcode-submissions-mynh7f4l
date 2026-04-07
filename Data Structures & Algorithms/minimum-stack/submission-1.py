class MinStack:

    def __init__(self):
        self.st = []
        self.m = []

    def push(self, val: int) -> None:
        self.st.append(val) 
        if self.m:
            self.m.append(min(self.m[-1], val))
        else:
            self.m.append(val)       

    def pop(self) -> None:
        self.st = self.st[:-1]
        self.m = self.m[:-1]

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.m[-1]
