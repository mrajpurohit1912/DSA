class stack:
    def __init__(self) -> None:
        self.stack = []
    
    def  is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self,data) ->None:
        self.stack.append(data)

    def print_stack(self):
        print(self.stack)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")
        
    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    stk = stack()
    # stk.push(1)
    # stk.push(2)
    # stk.push(3)
    # stk.print_stack()
    print(stk.is_empty())
    # print(stk.pop())
    # print(stk.pop())
    # print(stk.pop())
    # stk.print_stack()
    # print(stk.is_empty())