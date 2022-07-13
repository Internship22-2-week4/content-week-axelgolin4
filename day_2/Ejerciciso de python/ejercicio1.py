 
def contrasenaValida(a):
    if a == '2Fj(jjbFsuj' or a == 'eoZiugBf&g9':
        return "TRUE"

    else:
        return "FALSE"

print(contrasenaValida("2Fj(jjbFsuj")) # true
print(contrasenaValida("eoZiugBf&g9")) # true
print(contrasenaValida("hola")) # false
print(contrasenaValida("")) # false
