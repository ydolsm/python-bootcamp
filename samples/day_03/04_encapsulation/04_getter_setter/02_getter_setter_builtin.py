class ExampleClass:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("Accessed")
        return self._value

    @value.setter
    def value(self, value):
        print("Changed")
        self._value = value


example = ExampleClass(10)
example.value = 3
print(example.value)