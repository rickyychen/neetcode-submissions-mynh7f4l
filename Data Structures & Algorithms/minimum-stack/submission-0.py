class MinStack:

    def __init__(self):
        self.ms = []
        self.s = []

    def push(self, val: int) -> None:
        if self.ms and val > self.getMin():
            self.ms.append(self.getMin())
        else:
            self.ms.append(val)
        self.s.append(val)

    def pop(self) -> None:
        self.ms.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]
