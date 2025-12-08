import random

# Lista de palabras posibles
PALABRAS = [
    "PYTHON",
    "ENCEBOLLADO",
    "PROGRAMACION",
    "UIDE",
    "FRITADA",
    "INGENIERIA",
    "ENCRIPTADO"
]


def mostrar_estado(palabra, letras_correctas, letras_incorrectas, intentos_restantes):
    # Construir la palabra con guiones bajos y letras acertadas
    palabra_mostrada = " ".join(
        [letra if letra in letras_correctas else "_" for letra in palabra]
    )
    print("\nPalabra: ", palabra_mostrada)
    print("Intentos restantes:", intentos_restantes)
    if letras_incorrectas:
        print("Letras incorrectas:", " ".join(sorted(letras_incorrectas)))
    else:
        print("Letras incorrectas: (ninguna)")


def jugar_ahorcado():
    palabra = random.choice(PALABRAS)
    letras_correctas = set()
    letras_incorrectas = set()
    intentos_restantes = 6

    print("\n=== Nuevo juego del Ahorcado ===")

    