# Definimos una clase llamada Game

class Game:
    #Funcion constructora de la clase 
    def __init__(self, player_name):
        self.player_name = player_name  
        self.playing = False  
        self.arrangements_count = 0  # Contador de ordenamientos               
    
    #Funcion de ordenamiento, se inicia el tamaño de la lista y se le asigna el valor de la 
    #longitud de la lista se hace un ciclo for que va desde 0 hasta el tamaño de la lista, 
    # y otro ciclo for que va desde 0 hasta el tamaño de la lista menos i menos 1     
    def bubble_sort(self, list):
        n = len(list)  
        for i in range(n):
            for i_compared in range(0, n - i - 1):
                if list[i_compared] > list[i_compared + 1]:
                    list[i_compared], list[i_compared + 1] = list[i_compared + 1], list[i_compared]
        self.arrangements_count += 1  # Incrementar el contador de ordenamientos
        return list 

    def show_statistics(self):
        print(f"\nEstadísticas:")
        print(f"Total de listas ordenadas: {self.arrangements_count}")
    
    #Funcion para verificar si hay repetidos
    def repeats(self, list):
        return len(list) != len(set(list))

    #Funcion de iniciar juego, variable si es playing true significa que se ejecuto e inicio del juego
    #el usuario ingresa una lista de numeros separados por comas, se convierte a una lista de enteros
    #se imprime la lista original y se ordena con la funcion de ordenamiento, se imprime la lista si 
    #hay repetidos se imprime un mensaje de aviso, si no se imprime un mensaje de gracias por jugar
    #se termina el juego y luego la funcion para salir que se llama en el main
    def start_game(self):
        self.playing = True
        print(f"\n¡Bienvenido al juego, {self.player_name}!🎲")
        while self.playing:
            print("\nElige una opción:")
            print("1. Ordenar lista")
            print("2. Ver estadísticas")
            print("3. Salir del juego")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                entrada = input("Ingresa una lista de números separados por comas (ej: 5,2,9,1): ")
                try:
                    numeros = [int(userList.strip()) for userList in entrada.split(",")]
                    print(f"\nLista original: {numeros}")
                    ordered_list = self.bubble_sort(numeros)
                    print(f"Lista ordenada: {ordered_list}")
                    if self.repeats(ordered_list):
                        print("Aviso: Hay números repetidos en la lista ordenada.")
                except ValueError:
                    print("Error: Asegúrate de ingresar solo números separados por comas.")
            elif choice == "2":
                self.show_statistics()
            elif choice == "3":
                self.go_out()
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del menú.")

    def go_out(self):
        print(f"\nHasta luego, {self.player_name}. ¡Vuelve pronto!")
