from Autor import Autor
from Exposicion import Exposicion
from Obra import Obra
from Foto import Foto


#Ingresaremos un nuevo autor 
autor1 = Autor("Axel", "Rodas")
print("Se a ingresado el autor" )
print("Nombre: "+ autor1.nombre)
print(" Apellido:"+ autor1.apellido)

autor2 = Autor("Daniel", "Castillo")
print("Se a ingresado el autor Nombre:"+ autor2.nombre +" Apellido:"+ autor2.apellido)
print("Nombre: "+ autor2.nombre)
print(" Apellido:"+ autor2.apellido)

#Ingresaremos una nueva foto 
foto1 = Foto("Foto1", "12/07/2022", "www.foto1.com")
print("Se a ingresado la foto")
print("Nombre: "+ foto1.nombre)
print("Fecha: "+ foto1.fecha )
print("Uri: "+ foto1.uri)
print(" ")

#Ingresaremos una nueva obra 
obra1 = Obra("Fotografias", "Q200000",[autor1,autor2], foto1)
print("Se a ingresado una Obra Tipo:"+ obra1.tipo +" Precio:"+ obra1.valor)
print("Autores: "+ autor1.nombre + "  " + autor2.nombre)
print("fotos: " + foto1.nombre)
print(" ")

#Ingresaremos una nueva exposicion
exposicion1 = Exposicion("12/07/2022", "Quetzaltenango", "Exposicion nocturan para todo publico", obra1) 
print("Se a ingresado una Exposicion Fecha:"+ exposicion1.fecha +" Lugar:"+ exposicion1.lugar)
print("Descripcion: "+ exposicion1.descripcion)
print("Galeria: "+ exposicion1.galeria.tipo)
