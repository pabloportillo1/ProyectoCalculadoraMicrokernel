class MicroKernel:
    def __init__(self):
        self.operations = {}

    def register(self, operation):
        self.operations[operation.name()] = operation

    def execute(self, operation_name, a, b):
        if operation_name not in self.operations:
            raise ValueError("Operaation not found.")
        

        return self.operations[operation_name].execute(a, b)