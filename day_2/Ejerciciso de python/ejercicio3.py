def likes(like):
    if like < 1000:
        return like
    elif like > 1000 and like < 1000000:
        cadena = str(like)
        cont = 0
        resultado = ""
        total = ""
        for x in reversed(cadena):
            cont = cont + 1
            if cont >= 4:
                resultado = resultado + x
        
        for x in reversed(resultado):
            total = total + x
        
        return total + "K"
    else:
        cadena = str(like)
        cont = 0
        resultado = ""
        total = ""
        for x in reversed(cadena):
            cont = cont + 1
            if cont >= 7:
                resultado = resultado + x
        
        for x in reversed(resultado):
            total = total + x
        
        return total + "M"

print(likes(983)) # "983"
print(likes(1900)) # "1K"
print(likes(54000)) # "54K"
print(likes(120800)) # "120K"
print(likes(25222444)) # "25M"