class Example:

    def __init__(self, value):
        self._value = value
        self.read = True
        self.write = True

    def get_value(self):
        if self.read:
            return self._value
        else:
            raise Exception("Example has read disabled")

    def set_value(self, value):
        if self.write:
            self._value = value
        else:
            raise Exception("Example has write disabled")

example = Example(10)
example.set_value(20)

print(example.get_value())