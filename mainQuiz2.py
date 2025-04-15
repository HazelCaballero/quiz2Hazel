#Importacion del juego de cifrado
from Quiz2hazelP import Game

#Funcion para el menu
def show_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")   
    print("2. Salir")        
    print("======================")

#Funcion para asignar nombre, dar la bienvenida, o llamar a funcion de Game como start_game
# y go_out 
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
            game.go_out()
            running = False 
        else:
            print("Opción inválida. Intenta de nuevo.\n")
main()
