from core.operation_interface import Operation

class Divide(Operation):

    def name(self):
        return "divide"
    
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    