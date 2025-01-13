class Example:

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

example = Example(10)
example.set_value(20)

print(example.get_value())