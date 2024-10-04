import random

def adivina_num():
    secret_num = random.randint(1, 10)
    intents = 3
    print("Joc: Adivina un num (1 al 10) tens tres intents")
    
    while intents > 0:
        try:
            adivina = int(input(f"Intent {4 - intents}: Introdueix un num entre 1 i 10: "))
        except ValueError:
            print("Introdueix un num valid")
            continue
        
        if adivina < 1 or adivina > 10:
            print("Num fora de rang")
        elif adivina == secret_num:
            print(f"Oleee! Has endevinat el num {secret_num}")
            return
        else:
            if adivina < secret_num:
                print("El num es mes gran")
            else:
                print("El num es mes petit")
        intents -= 1
    
    print(f"Ho sento, has perdut, el num era {secret_num}.")

# Funció per al joc de Pedra-Paper-Tisores
def pedra_paper_tisores():
    opcions = ["pedra", "paper", "tisores"]
    points_usuari, points_maquina = 0, 0
    
    def determina_guanyador(usuari, maquina):
        if usuari == maquina:
            return "Empate"
        elif (usuari == "pedra" and maquina == "tisores") or (usuari == "paper" and maquina == "pedra") or (usuari == "tisores" and maquina == "paper"):
            return "Usuari"
        else:
            return "Maquina"
    
    print("Pedra, Paper, Tisores. Qui arribi a 3 punts guanya")
    
    while points_usuari < 3 and points_maquina < 3:
        usuari = input("Introdueix 'pedra', 'paper', o 'tisores': ").lower()
        if usuari not in opcions:
            print("Opcio no valida")
            continue
        
        maquina = random.choice(opcions)
        print(f"La eleccio de la maquina es: {maquina}")
        
        guanyador = determina_guanyador(usuari, maquina)
        if guanyador == "Usuari":
            points_usuari += 1
            print("Aquest punt es teu")
        elif guanyador == "Maquina":
            points_maquina += 1
            print("Punt per la maquina")
        else:
            print("Empate!")
        
        print(f"Punts - Usuari: {points_usuari}, Maquina: {points_maquina}")
    
    if points_usuari == 3:
        print("Olee! Has guanyat!")
    else:
        print("La maquina ha guanyat")

# joc del Penjat
def el_penjat():
    with open('paraules.txt', 'r') as fitxer:
        paraules = [linea.strip() for linea in fitxer.readlines()]
    
    paraula_secret = random.choice(paraules)
    intents = len(paraula_secret) * 2
    paraula_oculta = ["_"] * len(paraula_secret)
    lletres_endevinades = set()
    
    print("Joc: El Penjat.")
    
    while intents > 0 and "_" in paraula_oculta:
        print(f"Paraula: {' '.join(paraula_oculta)}")
        print(f"Tens {intents} intents")
        
        lletra = input("Introdueix una lletra: ").lower()
        if len(lletra) != 1 or not lletra.isalpha():
            print("Introdueix una lletra")
            continue
        if lletra in lletres_endevinades:
            print("Aquesta lletra ja esta probada")
            continue
        
        lletres_endevinades.add(lletra)
        
        if lletra in paraula_secret:
            for i, l in enumerate(paraula_secret):
                if l == lletra:
                    paraula_oculta[i] = lletra
            print(f"Olee! La lletra '{lletra}' esta dins de la paraula")
        else:
            intents -= 1
            print(f"La lletra '{lletra}' no esta a la paraula.")
    
    if "_" not in paraula_oculta:
        print(f"Oleee! Has endevinat la paraula: {''.join(paraula_oculta)}")
    else:
        print(f"Has perdut, la paraula era: {paraula_secret}")

# Funció principal per mostrar el menú
def menu():
    while True:
        print("\n--- Menu de Jocs ---")
        print("1. Adivina num")
        print("2. Pedra - Paper - Tisores")
        print("3. El Penjat")
        print("4. Sortir")
        
        try:
            opcio = int(input("Escull una opcio: "))
        except ValueError:
            print("Valor no valid, introdueix un num")
            continue
        
        if opcio == 1:
            adivina_num()
        elif opcio == 2:
            pedra_paper_tisores()
        elif opcio == 3:
            el_penjat()
        elif opcio == 4:
            print("Sortint del programa.")
            break
        else:
            print("Valor no valid, escull una opcio entre 1 i 4.")

# Executar el menú
if __name__ == "__main__":
    menu()
