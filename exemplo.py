from vendedor import Vendedor

vendedor = Vendedor('Victor', 0, 5000.0)

try:
    print(vendedor.calcular_salario_base())
except Exception as msg:
    print(msg)