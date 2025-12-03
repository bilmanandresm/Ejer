

espacio_libre_gb = 37   
#espacio_libre_gb = input("Por Favor Ingrese el espacion numerico que tiene la memoria. ")

if espacio_libre_gb < 10:
    print("¡Alerta! El espacio libre en disco es crítico. Requiere limpieza urgente")
elif 10 <= espacio_libre_gb <= 50:
    print("Advertencia: El espacio libre en disco es bajo. Considere realizar una revisión ")
else:
    print("El espacio libre en disco es adecuado.")
