# celsius fahreneit

def celsius_fahrenheit (a):
    return (a*9/5)+32


cel=float(input("Informe a temperatura em graus celsius:"))
print("O equivalente em fahrenheit é %5.2f" % celsius_fahrenheit(cel))
