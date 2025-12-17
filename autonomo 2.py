import random

# Lista de palabras 
lista_de_palabras = [ "PYTHON", "ENCEBOLLADO", "PROGRAMACION",
    "UIDE", "FRITADA", "INGENIERIA", "ENCRIPTADO"]

def juego(palabra):
    palabra_completa = "_" * len(palabra)
    estado_adivinado = False
    letras_correctas = []
    palabras_adivinadas = []
    intentos = 6

    print("\n=== ¡Juguemos al Ahorcado! ===")
    print(visual_ahorcado(intentos))
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

    
