def temperatura_media(temp_max, temp_min):
    media = (temp_max + temp_min) /2
    return media
temperatura_maxima = int(input("Ingrese temperatura maxima en grados:"))
temperatura_minima = int(input("Ingrese temperatura minima en grados:"))
media_del_dia = temperatura_media (temperatura_maxima, temperatura_minima)

print(f"La temperatura media es:{media_del_dia} °C")
