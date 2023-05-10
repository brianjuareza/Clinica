# Crear representación para insertar un nodo de un árbol binario

class Nodo:
	def __init__(self, dato):
		self.izquierda = None
		self.derecha = None
		self.dato = dato

# crear la función del recorrido por la izquierda o por la derecha

def insertar(raiz, nodo):
	if raiz is None:
		raiz = nodo
	else:
		if raiz.dato < nodo.dato:
			if raiz.derecha is None:
				raiz.derecha = nodo
			else:
				insertar(raiz.derecha, nodo)
		else:
			if raiz.izquierda is None:
				raiz.izquierda = nodo
			else:
				insertar(raiz.izquierda, nodo)

#Recorrido inorden "correcta"
def inorden(raiz):
	if raiz is not None:
		inorden(raiz.izquierda)
		print(raiz.dato)
		inorden(raiz.derecha)

# Recorrido Preorden de un arbol binario "cumple"
def preorden(raiz):
	if raiz is not None:
		print (raiz.dato)
		preorden(raiz.izquierda)
		preorden(raiz.derecha)

# Recorrido Preorden de un arbol binario
def postorden(raiz):
	if raiz is not None:
		postorden(raiz.izquierda)
		postorden(raiz.derecha)
		print (raiz.dato)





#Prueba de inserción con los siguientes datos
raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))

inorden(raiz)
print()
preorden(raiz)
print()
postorden(raiz)