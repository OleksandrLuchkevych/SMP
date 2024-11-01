class Action:
    def __init__(self):
        self.result = 0.0

    def input(self):
        pass  # This will be defined in Calculator

    def output(self):
        print(self.result)

    def verify(self):
        return isinstance(self.result, float)  # Check if result is a float
