from action import Action


class Calculator(Action):
    def __init__(self, number1: float = 0, number2: float = 0, operator: str = "+"):
        super().__init__()
        self.number1 = number1
        self.number2 = number2
        self.operator = operator

    def input(self):
        try:
            self.number1 = float(input("Enter first number: "))
            self.number2 = float(input("Enter second number: "))
            self.operator = input("Enter operation to perform (+, -, *, /, ^, %): ")
        except ValueError:
            print("Value should be a number, try again")
            self.input()  # Re-ask if there's an error

    def check_operator(self) -> bool:
        return self.operator in ["+", "-", "*", "/", "^", "%"]

    def calculate(self):
        if not isinstance(self.number1, float) or not isinstance(self.number2, float):
            raise TypeError("Inputs should be floats")

        if self.operator == "+":
            self.result = self.number1 + self.number2
        elif self.operator == "-":
            self.result = self.number1 - self.number2
        elif self.operator == "*":
            self.result = self.number1 * self.number2
        elif self.operator == "/":
            if self.number2 != 0:
                self.result = self.number1 / self.number2
            else:
                raise ZeroDivisionError("Cannot divide by zero")
        elif self.operator == "^":
            self.result = pow(self.number1, self.number2)
        elif self.operator == "%":
            self.result = self.number1 % self.number2

    def verify(self) -> bool:
        if not self.check_operator():
            print("You've entered the wrong operator, please try again.")
            return False
        if self.operator == "/" and self.number2 == 0:
            print("Number cannot be divided by zero, please try again.")
            return False
        return True

    def output(self):
        print(f"{self.number1} {self.operator} {self.number2} = {self.result}")

    def ask_to_repeat(self):
        choice = input("For one more calculation, type Y: ").lower()
        if choice == "y":
            self.start()

    def start(self):
        self.input()
        if self.verify():
            self.calculate()
            self.output()
            self.ask_to_repeat()
