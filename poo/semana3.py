#funcion calcular promedio semanal
def calcular_promedio_semanal():
    """Solicita temperaturas diarias y calcula el promedio semanal."""
    # Lista para guardar las medias diarias
    temperaturas_diarias = [] 
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print(" Calculadora de Promedio Climático Semanal")

    #bucle para pedir las temperaturas de cada dia
    for dia in dias_semana:
        try:
            #pedir temperatura maxima y minima
            temp_max = float(input(f"Introduce la temperatura máxima de {dia}: "))
            temp_min = float(input(f"Introduce la temperatura mínima de {dia}: "))

            #calcular la media diaria
            media_diaria = (temp_max + temp_min) / 2
            temperaturas_diarias.append(media_diaria) # Añadir la media diaria a la lista
            print(f"Media diaria de {dia}: {media_diaria:.2f}°C\n")

        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
             #termina la funcion si hay error
            return 

    #calcular promedio semanal usando la lista medias diarias
    if temperaturas_diarias: 
        #asegurarse de que la lista no esté vacía
        promedio_semanal = sum(temperaturas_diarias) / len(temperaturas_diarias)
        print(f"\n--- Resultado ---")
        print(f"El promedio de temperatura semanal es: {promedio_semanal:.2f}°C")
    else:
        print("No se ingresaron datos para calcular el promedio.")
#llamar la funcion
calcular_promedio_semanal()

