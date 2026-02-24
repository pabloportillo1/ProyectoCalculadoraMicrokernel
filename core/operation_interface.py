from abc import ABC, abstractmethod

class OperationInteface(ABC):
    @abstractmethod
    def execute(self, a, b):
        # Ejecuta la operacion con los operandos a y b, y regresa el resultado.
        pass

    @abstractmethod
    def get_name(self):
        # Regresa el nombre de la operaacion, por ejemplo : "Suma", "Resta", etc.
        pass