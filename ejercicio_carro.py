# algoritmo de velocidad y frenado de un auto
import time
print("Bienvenido a su test de velocidad, recuerde que su velocidad ideal en la ciudad es 60 km/h")
class carro():  # se crea la clase con la que vamos a trabajar
    def __init__(self, velocidad = 0):
        self.velocidad =velocidad
    def acelerar(self):
        while True:
            print("\na. Aumentar velocidad", "f.Frenar", "c. Velocidad Crucero")
            print("Su vehiculo esta detenido")
            accion = input("Usted que desea hacer: ")
            if(accion == "a" or accion== "A"):
                self.velocidad+=5
                print("Su velocidad es: ", self.velocidad)
            if(accion=="C" or accion=="c"):
                while(self.velocidad< 60 and self.velocidad>=0):
                    time.sleep(1.0)
                    self.velocidad+=5
                    print("su velocidad es: ",self.velocidad)
                while(self.velocidad > 60):
                    time.sleep(1.0)
                    self.velocidad-=5
                    print("su velocidad crucero es: ", self.velocidad)
            if(self.velocidad >=5 and accion == "F" or self.velocidad >=5 and accion == "f"):
                while(self.velocidad >=5):
                    print(f"La velocidad actual del auto es: ",self.velocidad)
                    accion = (input("Desea disminuir la velocidad? escriba si o no  "))
                    if (accion=="si"):
                        self.velocidad-=5
                    elif(accion=="no"):
                        break
mazda=carro()
mazda.acelerar()
