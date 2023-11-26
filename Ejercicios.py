# EJERCICIO  1 

numeros_divisibles = []

for numero in range(1500, 2701):

    if numero % 7 == 0 and numero % 5 == 0:
     
        numeros_divisibles.append(numero)

print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(numeros_divisibles)



# EJERCICIO  2
n_filas = 5


for i in range(n_filas):
    for j in range(i + 1):
        print("*", end=" ")
    print()


for i in range(n_filas - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# EJERCICIO  3
numeros = []

while True:
    desea_ingresar = input("Desea ingresar un número? (SI/NO): ").upper()

    if desea_ingresar == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif desea_ingresar == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, responda SI o NO.")

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {sum(1 for num in numeros if num % 2 == 0)}")
print(f"Cantidad de números impares: {sum(1 for num in numeros if num % 2 != 0)}")

# EJERCICIO  4
lista_alumnos = []

n_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for _ in range(n_alumnos):
    nombre_alumno = input("Ingrese el nombre del alumno: ")

    calificaciones = []

    for materia in range(1, 4):
        calificacion = float(input(f"Ingrese la calificación de la materia {materia} para {nombre_alumno}: "))
        calificaciones.append(calificacion)

    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}
    lista_alumnos.append(alumno)

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
# EJERCICIO  5
def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad

numero_ingresado = 15789000
digito = 0

cantidad_veces = contar_digitos(numero_ingresado, digito)

print(f"Número ingresado: {numero_ingresado} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {cantidad_veces}")

# EJERCICIO  6
a, b = 0, 1
print(a)

while b <= 50:
    print(b)
    a, b = b, a + b
# EJERCICIO  7
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
# EJERCICIO  8
def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un número entero no negativo: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es {resultado_factorial}.")
# EJERCICIO  9
texto_original = input("Ingrese una cadena de texto: ")
texto_modificado = ''.join(char for char in texto_original if char.lower() not in 'aeiouAEIOU')

print(f"Texto original: {texto_original}")
print(f"Texto modificado: {texto_modificado}")

# EJERCICIO  10
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

fecha_input = input("Ingrese la fecha (mes-día-año o Mes día, año): ")

partes = fecha_input.split()

if partes[0].isnumeric():
    mes = int(partes[0])
    dia = int(partes[1].rstrip(','))
    año = int(partes[2])
else:
    mes = meses.index(partes[0]) + 1
    dia = int(partes[1].rstrip(','))
    año = int(partes[2])

fecha_formateada = f"{año:04d}-{mes:02d}-{dia:02d}"

print(f"Fecha ingresada: {fecha_input}")
print(f"Fecha formateada: {fecha_formateada}")