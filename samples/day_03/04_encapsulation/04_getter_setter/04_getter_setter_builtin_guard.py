class ExampleClass:

    def __init__(self, value):
        self._value = value
        self.read = True
        self.write = True

    @property
    def value(self):
        if self.read:
            return self._value
        else:
            raise Exception("Example has read disabled")

    @value.setter
    def value(self, value):
        if self.write:
            self._value = value
        else:
            raise Exception("Example has write disabled")

example = ExampleClass(10)
example.value = 3
print(example.value)