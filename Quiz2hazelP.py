# Definimos una clase llamada Game
class Game:
    #Funcion constructora de la clase
    def __init__(self, player_name):
        self.player_name = player_name 
        self.playing = False  
        self.alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  
        
    #Funcion de encriptacion, se inicia el mensaje vacio, se cambia a mayusculas para evaluarlo 
    #para cada letra en el mensaje si esta en la variable alphabet se le tiene una variable con 
    #el indice origial, se le dice que le sume el desplazamiento y se usa modulo para tener un 
    #numero con un resultado estable con el que trabajar y evitar errores y se le asigna los
    #nuevos indices al mensage encriptado, si no es una letra se deja igual, al final se retorna
    def encryption_cesar(self, message, displacement):
        encrypted_message = ""  
        message = message.upper()  
        for caracter in message:
            if caracter in self.alphabet:
                original_index = self.alphabet.index(caracter)  
                encrypted_index = (original_index + displacement) % len(self.alphabet)  
                encrypted_message += self.alphabet[encrypted_index]  
            else:
                encrypted_message += caracter
        return encrypted_message  

    #Similar a la funcion anterior pero retrocede en el desplazamiento
    def desencryption_cesar(self, encrypted_message, displacement):
        message_decrypted = ""  
        encrypted_message = encrypted_message.upper()  
        for caracter in encrypted_message:
            if caracter in self.alphabet:
                encrypted_index = self.alphabet.index(caracter)
                original_index = (encrypted_index - displacement) % len(self.alphabet)
                message_decrypted += self.alphabet[original_index]
            else:
                message_decrypted += caracter 
        return message_decrypted

    #Funcion de iniciar juego, variable si es playing true significa que se ejecuto e inicio del juego 
    #se tienen la opcion de elgir si cifrar o decifrar, y el desplazamiento puede ser ingresado por 
    #el usuario, da resultado y vuelve al menu y esta la funcion para terminar el juego que es usada en el main
    def start_game(self):
        self.playing = True  
        print(f"\n¡Bienvenido al juego, {self.player_name}!")
        print("El juego ha comenzado\n")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        choice = input("Seleciona una opción: ")
        message = input("\nEscribe el mensaje: ").upper()  
        while True:
            try:
                displacement = int(input("Escribe el número de desplazamiento (ej: 2): "))
                break  
            except ValueError:
                print("Por favor, ingresa un número válido.")  
        if choice == "1":
            result = self.encryption_cesar(message, displacement)
            print(f"\nMensaje cifrado: {result}")
        elif choice == "2":
            result = self.desencryption_cesar(message, displacement)
            print(f"\nMensaje descifrado: {result}")
        else:
            print("Opción inválida. Volviendo al menú.")
        print("\n¡Gracias por jugar!\n")

    def go_out(self):
        print(f"\nHasta luego, {self.player_name}. ¡Vuelve pronto!")
