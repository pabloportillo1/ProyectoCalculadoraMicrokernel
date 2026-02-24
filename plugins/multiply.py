from core.operation_interface import Operation

class Multiply(Operation):

    def name(self):
        return "multiply"
    
    def execute(self, a, b):
        return a * b
    