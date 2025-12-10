class ClimaDiario:
    #Clase que representa la información diaria del clima.

    def __init__(self, dia, temperatura):
        # Encapsulamiento: atributos privados
        self.__dia = dia
        self.__temperatura = temperatura

    def obtener_dia(self):
        #Metodo getter para acceder al día.
        return self.__dia

    def obtener_temperatura(self):
        #Metodo getter para acceder a la temperatura.
        return self.__temperatura


class SemanaClima:
    #Clase que representa la semana completa de clima.
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia, temperatura):
        #Agrega un objeto ClimaDiario con día y temperatura.
        self.dias.append(ClimaDiario(dia, temperatura))

    def calcular_promedio(self):
        #Calcula el promedio semanal de las temperaturas.
        total = sum(dia.obtener_temperatura() for dia in self.dias)
        return total / len(self.dias)

    def mostrar_temperaturas(self):
        #Muestra todas las temperaturas registradas con su día.
        for dia in self.dias:
            print(f"{dia.obtener_dia()}: {dia.obtener_temperatura()} °C")


def main():
    print("=== Promedio Semanal del Clima (POO con días) ===")
    semana = SemanaClima()
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias_semana:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        semana.agregar_dia(dia, temp)

    print("\nTemperaturas registradas:")
    semana.mostrar_temperaturas()

    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()