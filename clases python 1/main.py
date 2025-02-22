from Clases.Animal import Animal
from Clases.Ave import Ave

x = Animal("Rocki", "15 kg")
p = x.imprimirnombre()
print(p)


x2 = Ave(" la paloma", "5 kg", 2006, "Jay-Z Valencia")  
print(x2.imprimiraño_nacimiento())


print(x2.calcular_edad(2025)) 