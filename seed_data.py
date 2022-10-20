from primerMVT.models import Familiar

Familiar(nombre="Antonio", direccion="Dto Alvarez 7373", numero_pasaporte=123456).save()
Familiar(nombre="Matias", direccion="Dto Alvarez 7373", numero_pasaporte=654321).save()
Familiar(nombre="Estefany", direccion="Emilio Zola 7884", numero_pasaporte=345678).save()
Familiar(nombre="Gaston", direccion="Emilio Zola 7884", numero_pasaporte=234567).save()

print("Se cargo con éxito los usuarios de pruebas")