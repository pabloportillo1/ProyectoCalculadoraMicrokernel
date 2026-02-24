from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def execute(self, a, b):
        pass