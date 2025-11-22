class Masa:
    
    def __init__(self):
        pass

    def kg_lb(self):
        
        # Funcion para convertir kilogramos a libras 

        print("=== Kilogramos a Libras ===")

        kg = float(input("KG: "))
        lb = kg * 2.2046
        print(f"{kg:.2f} Kg son {lb:.2f} libras")

    def lb_kg(self):
        
        # Funcion para convertir libras a kilogramos 

        print("=== Libras a Kilogramos ===")

        lb = float(input("LB: "))
        kg = lb * 0.4536
        print(f"{lb:.2f} libras son {kg:.2f} Kg")

    def menu(self):

        # Muestra el menú de opciones de masa 

        print("\n=== MASA ===\n")
        print("1 - Kilogramos a Libras")
        print("2 - Libras a Kilogramos")
        print("3 - Volver al menú principal")
        print("\nPor favor, seleccione una opcion del menú:\n")
        print("=" * 20)
        print("\n")

    def menu_main(self):

        # Función principal del menú de masa 

        while True:
            self.menu()
            option = input("\nSelecciona una opcion: \n")

            if option == "1":
                self.kg_lb()
                pausar()

            elif option == "2":
                self.lb_kg()
                pausar()

            elif option == "3":
                # Volver a Menu Principal
                return

            else:
                self.print("Por favor, seleccione una opcion del menú.")
                pausar()
