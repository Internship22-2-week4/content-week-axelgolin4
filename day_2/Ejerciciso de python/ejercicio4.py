def bmi(peso , altura ):
    calculado = peso / altura ** 2

    if calculado < 18.5:
        return "Bajo de peso"
    if calculado >= 18.5 and calculado <= 24.9:
        return "Normal"
    if calculado >= 25 and calculado <= 29.9:
        return "Sobre peso"
    if calculado > 30:
        return "Obeso"

    else:
        return 0

print(bmi(65, 1.8)) # "Normal"
print(bmi(72, 1.6)) # "Sobrepeso"
print(bmi(52, 1.75)) #  "Bajo de peso"
print(bmi(135, 1.7)) # "Obeso"