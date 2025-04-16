def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Ejemplo de uso
anio = int(input("Ingresa un año: "))
if es_bisiesto(anio):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
