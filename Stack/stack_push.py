def push(self, data):
    if len(self.stack) >= self.limit:
        raise IndexError('overflow the stack")
        self.stack.append(data)
