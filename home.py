

from typing import Any


class LogicGates:
    """Logic gates for the game"""

    def __init__(self, input_number, ) -> None:
        self.input_number = input_number
        self.inputs = []
        if self.input_number > 26:
            raise ValueError("Input number cannot be greater than 26")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # check if self.input_number is valid and is not greater than the number of all capital letters on class call
        if self.input_number > 26:
            raise ValueError("Input number cannot be greater than 26")
        return self.generate_input()

    def generate_input(self):
        """Generate input for the logic gates based on the input number, the inputs should be capital letters from A to Z"""
        for i in range(self.input_number):
            self.inputs.append(chr(65+i))
        return self.inputs

    def __repr__(self) -> str:
        return f"LogicGates({self.input_number})"

    def generate_truth_table(self):
        """Generate truth table for the logic gates"""
        pass


v = LogicGates(5)
print(LogicGates(5))
