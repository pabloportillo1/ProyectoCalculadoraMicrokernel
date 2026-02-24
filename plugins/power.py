from core.operation_interface import Operation

class Power(Operation):

    def name(self):
        return "power"
    
    def execute(self, a, b,):
        return a ** b
    