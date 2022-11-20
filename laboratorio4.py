#!/usr/bin/python3
# IE-0117 Programación Bajo Plataformas Abiertas
# Francisco Moya Mena
# Carnet A74449
# Creación de clase para representar un vector de n elementos


class Vector():  # Se crea la clase

    def __init__(self, tamaño, value=""):
        if type(tamaño) != int or int(tamaño) < 0:  # Restricciones tamaño
            raise ValueError("\n\nPara el tamaño del vector ingrese un"
                             " valor entero positivo\n\n"
                             )
        self.tamano = tamaño  # Se define el tamaño
        if value == "":  # Restricciones  valores iniciales vector
            self.value = [0]*int(tamaño)
        else:
            if type(value) != list or len(value) != self.tamano:
                raise TypeError(
                                "\n\nPara los valores del vector ingrese"
                                " una lista de {} números"
                                " reales\n\n"
                                . format(self.tamano,)
                                )
            for dato in range(len(value)):
                if type(value[dato]) != float:
                    raise TypeError(
                                    "\n\nPara los valores del vector ingrese"
                                    " una lista de {}"
                                    " números reales\n\n". format(self.tamano)
                                    )
        self.value = value  # Se definen  valores iniciales  vector

    def __setitem__(self, value, newvalue):
        if type(newvalue) != float:  # Restricciones valores indexados vector
            raise ValueError("\n\nPara los valores del vector ingrese un"
                             " número real\n\n"
                             )
        if type(value) != int or value < 0 or value >= self.tamano:
            raise ValueError("\n\nIndice inválido\n\nIngrese un número entero"
                             " positivo entre: 0 y {}"
                             "\n\n". format(self.tamano-1)
                             )

        self.value[value] = newvalue  # Se definen valores indexados vector

    def __getitem__(self, value):
        if type(value) != int or value < 0 or value >= self.tamano:
            raise ValueError("\n\nIndice inválido\n\n Ingrese un número entero"
                             " positivo entre 0 y {}"
                             "\n\n". format(self.tamano-1)
                             )
        return self.value[value]  # Se obtienen valores indexados vector

    def __str__(self):
        return "{}".format(self.value)  # Se obtiene vector como  string

    def __add__(self, other):
        componente = []
        if len(self.value) != len(other.value):  # Restricciones suma vectores
            raise ValueError("\n\nEl tamaño de los vectores es distinto"
                             " \n\nPrimer vector: {} \nSegundo vector: {}\n\n"
                             . format(self.tamano, other.tamano)
                             )
        for dato in range(len(self.value)):
            componente.append(self.value[dato] + other.value[dato])
        return Vector(self.tamano, value=componente)

    def __len__(self):
        return len(self.value)


if __name__ == '__main__':
    vectorA = Vector(3, value=[1.0,  -3.6, 4.5])
    vectorA[1] = 2.0
    vectorB = Vector(3, value=[2.8, 2.8, 6.4])
    vectorC = vectorA + vectorB

    print(vectorA)
    print(vectorA[2])
    print(vectorB)
    print(vectorB[2])
    print(vectorC)
    print(vectorC[2])
    print(len(vectorC))
