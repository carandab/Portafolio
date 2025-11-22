class Volumen:
    def __init__(self):
        pass
    
    def lt_gal(self):
        
        # Función para convertir litros a galones US 

        print("=== Litros a Galones US ===")
        l = float(input("Litros: "))
        gal = l * 0.2642
        print(f"{l} litros son {gal:.2f} galones US")

    def gal_lt(self):
        
        # Función para convertir galones US a litros 

        print("=== Galones US a Litros ===")
        gal = float(input("Galones US: "))
        l = gal * 3.7854
        print(f"{gal} galones US son {l:.2f} litros")

    def ml_oz(self):
        
        # Función para convertir mililitros a onzas fluidas 

        print("=== Mililitros a Onzas Fluidas ===")
        ml = float(input("Mililitros: "))
        fl_oz = ml * 0.0338
        print(f"{ml} ml son {fl_oz:.2f} fl oz")

    def oz_ml(self):
        
        # Función para convertir onzas fluidas a mililitros 

        print("=== Onzas Fluidas a Mililitros ===")
        fl_oz = float(input("Onzas fluidas: "))
        ml = fl_oz * 29.5735
        print(f"{fl_oz} fl oz son {ml:.2f} ml")

    def menu(self):
        
        # Muestra el menú de opciones de volumen 

        print("\n=== VOLUMEN ===\n")
        print("1 - Litros a Galones US")
        print("2 - Galones US a Litros")
        print("3 - Mililitros a Onzas Fluidas")
        print("4 - Onzas Fluidas a Mililitros")
        print("5 - Volver al menú principal")
        print("\nPor favor, seleccione una opcion del menú:\n")
        print("=" * 20)
        print("\n")

    def menu_main(self):
        
        # Función principal del menú de volumen

        while True:
            self.menu()
            option = input("\nSelecciona una opcion: \n")

            if option == "1":
                self.lt_gal()
                pausar()

            elif option == "2":
                self.gal_lt()
                pausar()

            elif option == "3":
                self.ml_oz()
                pausar()

            elif option == "4":
                self.oz_ml()
                pausar()

            elif option == "5":
                # Volver a Menu Principal
                return

            else:
                print("Por favor, seleccione una opcion del menú.")
                pausar()


