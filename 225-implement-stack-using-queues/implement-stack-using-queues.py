class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        itm = self.stack[-1]
        self.stack.pop()
        return itm

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.stack == []