class queue:
    def  __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("No element to pop from queue")
        
    def peek(self):
        if not self.is_empty():
            print(self.queue[-1])
        else:
            raise IndexError("No element in queue")
    def print_queue(self):
        print(self.queue)

    def size(self):
        return len(self.queue)



if __name__ == "__main__":
    q = queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.is_empty())
    q.print_queue()
