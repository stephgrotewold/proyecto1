import cProfile
from Queue import  *
products=[]
cProfile.run('enqueue(products, "Esteban", "Zona16", 35351054)')
cProfile.run('dequeue(products)')
cProfile.run('IsEmpty(products)')
cProfile.run('Empty(products)')
