from core.operation_interface import Operation 

class Add(Operation):

    def name(self):
        return "add"
    
    def execute(self, a ,b):
        return a + b
    
    