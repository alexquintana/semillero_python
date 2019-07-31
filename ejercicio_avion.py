# Algoritmo para vuelo avion
import time
print("Aeropuerto Rafael Nuñez,\nPiloto puede solicitar permiso para confirmación a controlador para vuelo Cartagena-Bogotá\n")
time.sleep(1.5)
class avion():
    def __init__(self, vel = 0):
        self.vel= vel
        self.desp= 0
        self.flaps= 0
        self.pil="si"
    def pista(self):
        while True:
            contr ="si"
            contr =input("controlador, ¿ Me puede confirmar pista despejada? si o no : ")
            if (contr=="no"):
                print("esperando confirmación de pista")
            elif(contr =="si" or contr =="Si"):
                print("Piloto debe avanzar a pista para prepararse para despegue ")
                time.sleep(2.0)
                break
        print("Se deben seguir los preparativos para despegar, primer paso bajar los flaps")
        time.sleep(2.0)
        print("Controlador: piloto debe bajar los flaps a -3")
        time.sleep(1.50)
        for self.flaps in range (0,-4,-1):
            time.sleep(0.45)
            print("bajando flaps",self.flaps)
        time.sleep(1.50)
        print("Piloto: los flags estan en posición: ",self.flaps)
        time.sleep(1.50)
        if (self.flaps== -3):
            print("Controlador:preparese para para acelerar y despegar ")
            time.sleep(2.0)
            print("Piloto: Confirmado, gracias controlador ")
            time.sleep(1.50)
        while(self.vel< 180 and self.vel>=0):
            self.vel+=30
            time.sleep(0.45)
            print("Su velocidad es de: ",self.vel,"Km/h")
        print("Alcanzo la velocidad necesaria: ",self.vel,"Km/h")
        print("Ya esta en el aire ")
    def pilo(self):
            self.pil=input("Controlador: Piloto ¿Desea subir los flaps a 0, y subir el tren de aterrizaje? si o no :  ")
            while (self.pil=="no" or "No" or "NO"):
                if(self.pil=="no"):
                    print("¡cuidado esta aumentando la resistencia, su rendimiento de vuelo es bajo, corrija para mejorar su vuelo!")
                    self.pil=input("Controlador: Piloto ¿Desea subir los flaps a 0, y subir el tren de aterrizaje? si o no :  ")
                    print("¡Usted pierde altitud! ¡falla total del sistema! ¡Va a estrellarse!")
                    time.sleep(2.0)
                    print(" las investigaciones indican que el accidente fue un error humano, no hubo sobrevivientes")
                    break
                elif(self.pil=="si"):
                    print("¡Perfecto!, Feliz vuelo")
                    break

a=avion()
a.pista()
a.pilo()
