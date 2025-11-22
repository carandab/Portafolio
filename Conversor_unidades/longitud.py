class Longitud:

    def __init__ (self):
        pass

    # Metodos

    def m_ft(self):
        # Función para convertir metros a pies con formato ft'inch" 

        print("=== Metros a Pies y Pulgadas ===")
        m = float(input("M: "))
        ft_total= m * 3.2808

        # Separar pies enteros de la parte decimal
        ft_enteros = int(ft_total)
        ft_decimal = ft_total - ft_enteros

        # Convertir la parte decimal a pulgadas (12 pulgadas = 1 pie)
        pulgadas = ft_decimal * 12

        print(f"{m} metros = {ft_enteros}'{pulgadas:.2f}\"")

    def ft_m(self):
        # Función para convertir ft'inch" a metros 

        print("=== Pies y Pulgadas a Metros ===")
        ft = int(input("Pies: "))
        inch = float(input("Pulgadas: "))

        # Convertir todo a pies decimales
        ft_total = ft + (inch / 12)

        # Convertir a metros
        m = ft_total * 0.3048

        print(f"{ft}'{inch:.2f}\" son {m:.2f} metros")

    def km_millas(self):
        # Función para convertir kilómetros a millas 

        print("=== Kilómetros a Millas ===")
        km = float(input("Kilómetros: "))
        millas = km * 0.6214
        print(f"{km} km son {millas:.2f} millas")

    def millas_km(self):
        # Función para convertir millas a kilómetros 

        print("=== Millas a Kilómetros ===")
        millas = float(input("Millas: "))
        km = millas * 1.6093
        print(f"{millas} millas son {km:.2f} km")


    def menu(self):
            
        print("\n=== LONGITUD ===\n")
        print("1 - Pies a Metros")
        print("2 - Metros a Pies")
        print("3 - Kilómetros a Millas")
        print("4 - Millas a Kilómetros")
        print("5 - Volver al menú principal")
        print("\nPor favor, seleccione una opcion del menú:\n")
        print("=" * 20)
        print("\n")
    
    def menu_main(self):
            
        while True:
            self.menu()
            option = input("\nSelecciona una opcion: \n")

            if option == "1":
                self.ft_m()
                pausar()

            elif option == "2":
                self.m_ft()
                pausar()

            elif option == "3":
                self.km_millas()
                pausar()

            elif option == "4":
                self.millas_km()
                pausar()

            elif option == "5":
                # Volver a Menu Principal
                return

            else:
                print("Por favor, seleccione una opcion del menú.")
                pausar()

