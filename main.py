from core import microkernel
from plugins.add import Add
from plugins.multiply import Multiply
from plugins.substract import Substract
from plugins.power import Power
from plugins.divide import Divide

from core.microkernel import MicroKernel
from core.operation_interface import Operation

def main():

    kernel = MicroKernel()

    kernel.register_operation(Add())
    kernel.register_operation(Multiply())
    kernel.register_operation(Substract())
    kernel.register_operation(Power())
    kernel.register_operation(Divide())

    while True:
        print("\nAvailable operations:", list(kernel.operations.keys()))
        op_name = input("Enter operation name or 'exit to quit: ")

        if op_name == "exit":
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter sencond number: "))
            result = kernel.execute_operation(op_name, a, b)
            print(f"result: {result}")
        except Exception as e:
            print(f"Error: ", e)

if __name__ == "__main__":
    main()