def areaTriangulo(altura,base):
    return (base*altura)/2

def areaCirculo(radio):
    PI=3.141592
    return round(PI*(radio*radio),2)
print("El area del triangulo es: ",areaTriangulo(20,30))
print("El area del circulo es: ",areaCirculo(25))