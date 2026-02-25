from core.operation_interface import Operation

class Modulo(Operation):

    def name(self):
        return "mod"

    def execute(self, a, b):
        return a % b