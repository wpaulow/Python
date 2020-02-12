frase = input("Digite uma frase: ").lower()
a = frase.count("a")
e = frase.count("e")
i = frase.count("i")
o = frase.count("o")
u = frase.count("u")
total = a + e + i + o + u
print("Esta frase tem %d vogais!" % total)
