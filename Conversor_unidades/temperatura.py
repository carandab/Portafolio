class Temperatura:

    def __init__(self):
        pass

    # Metodos

    
    def celsius_fahrenheit(self):
        # Función para convertir Celsius a Fahrenheit 

        print("=== Celsius a Fahrenheit ===")
        c = float(input("°C: "))
        f = (c * 9/5) + 32
        print(f"{c}°C son {f}°F")

    def fahrenheit_celsius(self):
        # Función para convertir Fahrenheit a Celsius 

        print("=== Fahrenheit a Celsius ===")
        f = float(input("°F: "))
        c = (f - 32) * 5/9
        print(f"{f}°F son {c:.2f}°C")

    def menu(self):

        print("\n=== TEMPERATURA ===\n")
        print("1 - Celsius a Fahrenheit")
        print("2 - Fahrenheit a Celsius")
        print("3 - Volver al menú principal")
        print("\nPor favor, seleccione una opcion del menú:\n")
        print("=" * 20)
        print("\n")

    def menu_main(self):
        # Función principal del menú de temperatura 

        while True:
            self.menu()
            option = input("\nSelecciona una opcion: \n")

            if option == "1":
                self.celsius_fahrenheit()
                pausar()

            elif option == "2":
                self.fahrenheit_celsius()
                pausar()

            elif option == "3":
                # Volver a Menu Principal
                return

            else:
                print("Por favor, seleccione una opcion del menú.")
                pausar()
