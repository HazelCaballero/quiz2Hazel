from Quiz2hazelP import Game

def show_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")   
    print("2. Salir")        
    print("======================")

def main():
    name = input("Ingresa tu nombre para comenzar: ")
    game = Game(name)
    running = True
    
    while running:
        show_menu()
        opcion = input("Seleciona una opción: ")
        if opcion == "1":
            game.start_game()
        elif opcion == "2":
            game.salir()
            running = False 
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()
