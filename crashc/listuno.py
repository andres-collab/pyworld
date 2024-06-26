listado = ["Nueva York", "Chicago", "Boston", "Miami"]
print(listado)
listadoInvertido = listado[::-1]
print(listadoInvertido)

listadoInvertido.sort()
listadoInvertido.reverse()
revertido = listadoInvertido

revertido.append("San Francisco")

print(revertido.pop())
print(sorted(revertido))

print(listadoInvertido)
listadoInvertido.sort(reverse=True)
listadoInvertido.remove("Boston")
print(listadoInvertido)
del (listadoInvertido[0])
listadoInvertido.sort()
print(listadoInvertido)
