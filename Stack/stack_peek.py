def peek(self):
    if self.stack:
        return self.stack[-1]
def is_empty(self):
    return not bool(self.stack)
def size(self):
    return len(self.stack)
