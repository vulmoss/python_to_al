def pop(self):
    if self.stack:
        return self.stack.pop()
    else:
        raise IndexError('pop from an empty stack')

