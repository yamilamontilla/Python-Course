calificacion = int(float(input('Introduce la nota del alumno:  ')))

if calificacion >= 9:
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif calificacion >= 7 and calificacion < 9:
    print("Has aprobado satisfactoriamente.")
elif calificacion >= 5 and calificacion < 7:
    print("Has aprobado, pero necesitas mejorar un poco.")
else:
    print("Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")