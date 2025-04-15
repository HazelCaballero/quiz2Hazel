#Importacion del juego de cifrado y BubbleSort desde 2 archivos diferentes
from Quiz2hazelP import Game as JuegoCifrado  
from Quiz2hazelC import Game as JuegoBubbleSort

#Funcion para el menu
def show_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego de Ordenamiento")
    print("2. Iniciar juego de Cifrado César")
    print("3. Salir")
    print("======================")

#Funcion para asignar nombre, dar la bienvenida, o llamar a funciones de Game como start_game
# y go_out, se establecen 2 opciones para poder ejecutar los 2 juegos
# y se termina el juego con la opcion 3 para salir
def main():
    name = input("Ingresa tu nombre para comenzar: ")
    running = True
    game1 = JuegoBubbleSort(name)
    game2 = JuegoCifrado(name)
    while running:
        show_menu()
        opcion = input("Seleciona una opción: ")
        if opcion == "1":
            game1.start_game()
        elif opcion == "2":
            game2.start_game() 
        elif opcion == "3":
            print(f"\nHasta luego, {name}. ¡Vuelve pronto!")
            running = False 
        else:
            print("Opción inválida. Intenta de nuevo.\n")
main()
