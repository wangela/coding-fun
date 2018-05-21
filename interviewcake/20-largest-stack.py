class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):
    # [1, 2, 3, 4]
    # [4, 3, 2, 1]

    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        if item > self.max:
            self.max_stack.push(item)
        self.stack.push(item)

    def pop(self):
        if not self.stack.items:
            return None

        popped = self.items.pop()
        if popped == self.max_stack                                                                                                                                                                                                                                                                                                                                .peek():
            self.max_stack.pop()
            self.max = self.max_stack.pop()

        return popped

    def reset_max(self):
        if not self.stack.items:
            return None

        sorted_stack = sorted(self.stack.items, reverse = True)
        return sorted_stack[0]

    def get_max(self):
        return self.max
