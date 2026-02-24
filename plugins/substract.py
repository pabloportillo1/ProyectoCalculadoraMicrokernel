from core.operation_interface import Operation

class Substract(Operation):

    def name(self):
        return "substract"
    
    def execute(self, a, b):
        return a - b
    
    