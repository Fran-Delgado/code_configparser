# code_configparser.py
import configparser

config = configparser.ConfigParser()
config.read("fichero.ini")

# lista 
secciones = config.sections()
print(secciones)

# lista
opciones_3 = config.options('Seccion_3')
print(opciones_3)

# str
valor = config.get('Seccion_2', 'Valor_3')
print(valor)
