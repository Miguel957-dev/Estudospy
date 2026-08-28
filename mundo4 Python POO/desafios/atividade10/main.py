from frete import *

def main():
    mot = Moto(50 )
    mot.calcula_frete()
    cab = Caminhao(100)
    cab.calcula_frete()
    arduino = Drone(7)
    arduino.calcula_frete()

if __name__ == "__main__":
    main()