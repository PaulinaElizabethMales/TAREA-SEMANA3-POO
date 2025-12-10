
def ingresar_temperaturas():

    #Función para ingresar las temperaturas diarias de la semana,asociando cada temperatura con el día correspondiente.
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []

    for dia in dias_semana:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        # Guardamos como tupla (día, temperatura)
        temperaturas.append((dia, temp))

    return temperaturas


def calcular_promedio(temperaturas):
    #Calcula el promedio semanal a partir de la lista de tuplas (día, temperatura).
    total = sum(temp for _, temp in temperaturas)
    return total / len(temperaturas)


def main():
    print("=== Promedio Semanal del Clima con días de la semana ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print("\nTemperaturas registradas:")
    for dia, temp in temperaturas:
        print(f"{dia}: {temp} °C")

    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()