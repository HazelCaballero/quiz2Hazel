#Importacion del juego de ordenamiento
from Quiz2hazelC import Game

#Funcion para el menu
def show_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar game")   
    print("2. Salir")          
    print("======================")

#Funcion para asignar name, dar la bienvenida, o llamar a funcion de Game como start_game
# y go_out 
def main():
    name = input("Ingresa tu name para comenzar: ")
    game = Game(name)
    running = True
    while running:
        show_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            game.start_game()
        elif opcion == "2":
            game.go_out()
            running = False  
        else:
            print("Opción inválida. Intenta de nuevo.\n")
main()

