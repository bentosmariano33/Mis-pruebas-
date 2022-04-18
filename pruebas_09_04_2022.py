def tipoTriangulo(x, y, z):
    if not ((x>0) and (y>0) and (z>0))and ((x+y)!=z):
        return "No es un triangulo"
    elif ((x==y)and(y==z)):
        return "Equilatero"
    elif ((x!=y)and(x!=z)and(y!=z)):
        return "Escaleno"
    elif((x+y)!=z) or ((y+z)!=x) or ((x+z)!=y):
        return "Isosceles"
    
print(tipoTriangulo(2,2,5))