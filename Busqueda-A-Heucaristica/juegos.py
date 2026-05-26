import random
import os

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def dilema_del_prisionero():
    limpiar_pantalla()
    print("\n=== 1. EL DILEMA DEL PRISIONERO ===")
    print("Dos sospechosos son arrestados. Si ambos callan, cooperan.")
    print("Si uno traiciona, sale libre y el otro recibe la pena máxima.")
    input("\nPresiona Enter para ver la decisión estratégica...")
    
    opciones = ['Cooperar', 'Traicionar']
    j1, j2 = random.choice(opciones), random.choice(opciones)
    
    print(f"\n> Jugador 1 eligió: {j1}")
    print(f"> Jugador 2 eligió: {j2}")
    
    if j1 == 'Cooperar' and j2 == 'Cooperar':
        print("\nRESULTADO: Ambos reciben 1 año (Cooperación exitosa).")
    elif j1 == 'Traicionar' and j2 == 'Traicionar':
        print("\nRESULTADO: Ambos reciben 2 años (Equilibrio de Nash ineficiente).")
    else:
        traidor = "Jugador 1" if j1 == 'Traicionar' else "Jugador 2"
        print(f"\nRESULTADO: El {traidor} sale libre; el otro recibe 3 años.")
    input("\nRegresar al menú principal...")

def juego_de_la_gallina():
    limpiar_pantalla()
    print("\n=== 2. JUEGO DE LA GALLINA (CHICKEN) ===")
    print("Dos conductores van de frente. El que gira primero es la 'gallina'.")
    print("Si ninguno gira, el resultado es un choque fatal.")
    input("\nPresiona Enter para ver el desenlace...")
    
    estrategias = ['Desviarse', 'Seguir Recto']
    j1, j2 = random.choice(estrategias), random.choice(estrategias)
    
    print(f"> Conductor 1: {j1}")
    print(f"> Conductor 2: {j2}")
    
    if j1 == 'Seguir Recto' and j2 == 'Seguir Recto':
        print("\nRESULTADO: ¡CHOQUE! Desastre total para ambos.")
    elif j1 == 'Desviarse' and j2 == 'Desviarse':
        print("\nRESULTADO: Ambos evitaron el choque. Empate.")
    else:
        ganador = "Conductor 1" if j1 == 'Seguir Recto' else "Conductor 2"
        print(f"\nRESULTADO: {ganador} gana prestigio; el otro pierde respeto.")
    input("\nRegresar al menú principal...")

def tragedia_de_los_comunes():
    limpiar_pantalla()
    print("\n=== 3. TRAGEDIA DE LOS COMUNES ===")
    print("5 pastores comparten un campo con capacidad para 100 ovejas.")
    print("Si el consumo total supera 100, el campo se erosiona y todos pierden.")
    input("\nPresiona Enter para ver la gestión del recurso...")
    
    limite = 100
    consumos = [random.randint(15, 25) for _ in range(5)]
    total = sum(consumos)
    
    print(f"\nConsumos individuales: {consumos}")
    print(f"Demanda total: {total} / Límite: {limite}")
    
    if total > limite:
        print("\nRESULTADO: ¡COLAPSO! El egoísmo agotó el recurso compartido.")
    else:
        print(f"\nRESULTADO: SOSTENIBLE. Sobran {limite - total} unidades de recurso.")
    input("\nRegresar al menú principal...")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("***************************************")
        print("* SIMULADOR DE TEORÍA DE JUEGOS    *")
        print("***************************************")
        print("1. El Dilema del Prisionero")
        print("2. Juego de la Gallina")
        print("3. Tragedia de los Comunes")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")
        
        if opcion == '1':
            dilema_del_prisionero()
        elif opcion == '2':
            juego_de_la_gallina()
        elif opcion == '3':
            tragedia_de_los_comunes()
        elif opcion == '4':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()