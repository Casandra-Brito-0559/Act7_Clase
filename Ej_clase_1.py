print("introduccion a clases")
class Animal:
    edad=2
    raza="Pitbull"
    comida="Croquetas"
    def come(self):
        print(f"Mi dog come "+self.comida)
    
print(Animal)
print("Creando al objeto de la clase Animal")
perro=Animal()
print(f"Edad de mi Dog {perro.edad}")
print(f"Raza de mi Dog {perro.raza}")
lacomida=perro.come()