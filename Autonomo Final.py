import random

# Lista de palabras 
lista_de_palabras = ["PYTHON", "ENCEBOLLADO", "PROGRAMACION",
    "UIDE", "FRITADA", "INGENIERIA", "ENCRIPTADO"]

def obtener_palabra_aleatoria():
    palabra = random.choice(lista_de_palabras)
    return palabra.upper()

# Dibujos del ahorcado (de menos a más errores)

def visual_ahorcado(intentos):
    etapas = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ========="""
    ]
    return etapas[6 - intentos]

# Esta es la funcion principal del juego
# Entrada en funcion de una letra
def juego(palabra):
    palabra_completa = "_" * len(palabra)
    estado_adivinado = False
    letras_correctas = []
    palabras_adivinadas = []
    intentos = 6

    print("\n=== ¡Juguemos al Ahorcado! ===")
    print(visual_ahorcado(intentos))
     print("\n=== solo se pueden ingresar letras===")
    print(palabra_completa)
    print("\n")

    while not estado_adivinado and intentos > 0:
        entrada = input("Por favor, escriba una letra o palabra: ").upper()

        if len(entrada) == 1 and entrada.isalpha():
            if entrada in letras_correctas:
                print(f"Ya adivinaste la letra {entrada}")
            elif entrada not in palabra:
                print(f"{entrada} no está en la palabra")
                intentos -= 1
                letras_correctas.append(entrada)
            else:
                print(f"¡Bien hecho! {entrada} está en la palabra")
                letras_correctas.append(entrada)
                lista_entrada = list(palabra_completa)
                indices = [i for i, letra in enumerate(palabra) if letra == entrada]
                for index in indices:
                    lista_entrada[index] = entrada
                palabra_completa = "".join(lista_entrada)
                if "_" not in palabra_completa:
                    estado_adivinado = True
# Entrada en funcion de una palabra
        elif len(entrada) == len(palabra) and entrada.isalpha():
            if entrada in palabras_adivinadas:
                print(f"Ya adivinaste la palabra {entrada}")
            elif entrada != palabra:
                print(f"{entrada} no es la palabra")
                intentos -= 1
                palabras_adivinadas.append(entrada)
            else:
                estado_adivinado = True
                palabra_completa = palabra
        else:
            print("No es un intento válido")

        print(visual_ahorcado(intentos))
        print(palabra_completa)
        print("\n")

    if estado_adivinado:
        print("¡Felicidades! ¡Ganaste el juego!")
    else:
        print(f"Lo siento, te quedaste sin intentos. La palabra era {palabra}")

def main():
    palabra = obtener_palabra_aleatoria()
    juego(palabra)
    while input("¿Quieres jugar de nuevo? (S/N): ").upper() == "S":
        palabra = obtener_palabra_aleatoria()
        juego(palabra)

if __name__ == "__main__":
    main()

