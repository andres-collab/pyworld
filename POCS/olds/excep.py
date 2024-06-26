first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except ZeroDivisionError as e:
    print("Esta operación no tira. No se puede dividir por 0 "+ e.__str__())

print("FIN.")
