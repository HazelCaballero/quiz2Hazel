class Game:
    
    def __init__(self, player_name):
        self.player_name = player_name 
        self.playing = False  
        self.alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  

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

    def start_game(self):
        self.playing = True  
        print(f"\n¡Bienvenido al juego, {self.player_name}!")
        print("El juego ha comenzado...\n")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        choice = input("Seleciona una opción: ")
        message = input("\nEscribe el mensaje: ").upper()  

        while True:
            try:
                displacement = int(input("Escribe el número de desplazamiento (clave): "))
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

    def salir(self):
        print(f"\nHasta luego, {self.player_name}. ¡Vuelve pronto!")
