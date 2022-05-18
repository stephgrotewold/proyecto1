import cProfile
from Encrypting import *
cProfile.run('encriptar("hola")')
cProfile.run('desencriptar(encriptar("hola"))')