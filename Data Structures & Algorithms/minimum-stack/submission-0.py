class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        #uses normal append to add onto stack
        self.stack.append(val)

    def pop(self) -> None:
        # Call pop() array method for last elem.
        self.stack.pop()


    def top(self) -> int:
        # just returns last elem of stack
        return self.stack[-1]


    def getMin(self) -> int:
        # use the min function to find min val
        return min(self.stack)
        
