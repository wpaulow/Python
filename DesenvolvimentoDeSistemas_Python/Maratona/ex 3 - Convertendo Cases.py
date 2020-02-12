def maiuscula (s):
    return s.upper()


def minuscula (s):
    return s.lower()


def capitalize (s):
    return s.title()



str = "O rato roeu a roupa do rei de Roma"

print(maiuscula(str))

print(minuscula(str))

print(capitalize(str))

st = str.lower()

print("O número de vogais na frase é " , st.count("a") + st.count("e") + st.count("i") + st.count("o") + st.count
("u") , ".")

print("O número de consoantes é: ", st.count("b") + st.count("c") + st.count("d") + st.count("f") + st.count("g") +
      st.count("h") + st.count("j") + st.count("k") + st.count("l") + st.count("m") + st.count("n") + st.count("p") +
      st.count("q") + st.count("r") + st.count("s") + st.count("t") + st.count("v") + st.count("x") + st.count("z") ,
      ".")


