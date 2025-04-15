class Juego:

    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador 
        self.jugando = False                  

    def bubble_sort(self, lista):
        n = len(lista)  
        for i in range(n):
            for i_comparado in range(0, n - i - 1):
                if lista[i_comparado] > lista[i_comparado + 1]:
                    lista[i_comparado], lista[i_comparado + 1] = lista[i_comparado + 1], lista[i_comparado]
        return lista  


    def iniciar_juego(self):
        self.jugando = True  

        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado...\n")


        print("\n¡Gracias por jugar!\n")


    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")
