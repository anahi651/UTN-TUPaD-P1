# Ejercicio 7: Cálculo del IMC (Índice de Masa Corporal)
# Objetivo: Aplicar fórmulas con variables numéricas ingresadas por el usuario.

# 1. Solicitar al usuario su peso en kg y su altura en metros.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# 2. Calcular el IMC con la fórmula: IMC = peso / (altura ** 2).
imc = peso / (altura ** 2)

# 3. Mostrar el resultado con un mensaje.
print(f"Tu IMC es: {imc:.2f}")  # Mostrar solo dos decimales para mayor claridad

# 4. Dar una recomendación según el IMC calculado
if imc < 18.5:
    print("Bajo peso: Debes subir de peso. Consulta con un profesional para una dieta adecuada.")
elif 18.5 <= imc <= 24.9:
    print("Peso saludable: ¡Tu peso es saludable, sigue así!")
elif 25.0 <= imc <= 29.9:
    print("Sobrepeso: Debes bajar de peso. Realiza ejercicio y consulta con un profesional de salud.")
else:
    print("Obesidad: Tu IMC está por encima de 30. Debes consultar a un profesional de salud, ya que tienes riesgo de enfermedades.")




