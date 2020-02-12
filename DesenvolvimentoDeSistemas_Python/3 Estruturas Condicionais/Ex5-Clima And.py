# Exemplo 5 - Utilizando o And
temp = float(input("Digite a temperatura atual"))
if temp <= 10:  # Se a temperatura for menor ou igual 10
    print("O clima está muito frio!")
elif temp > 10 and temp <= 20:  # Comparação normal usando AND
    print("O clima está frio!")
elif 20 < temp <= 25:  # Comparação simplificada, AND implicito
    print("O clima está agradável!")
elif 25 < temp <= 30:  # Comparação simplificada, AND implicito
    print("O clima está quente!")
else:  # Senão
    print("O clima está muito quente!")
