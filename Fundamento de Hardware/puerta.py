class puerta:
	altura=0
	anchura=0
	grosor=0
	nbisagra=0
	estado="cerrada"
	color="rojo"
	def __init__(self,a,b,g,n,c):
		self.altura=a
		self.anchura=b
		self.grosor=g
		self.nbisagra=n
		self.color=c
	def abrir(self):
		self.estado="abierta"
	def cerrar(self):
		self.estado="cerrado"
	def muestra(self):
		print "ancho:",self.anchura
		print "alto:",self.altura
		print "grosor:",self.grosor
		print "nbisagra:",self.nbisagra
		print "color:",self.color
		print "estado:",self.estado

	def __add__(self,puerta2):
		t=puerta(0,0,0,0,"verde")
		t.altura=self.altura+puerta2.altura
		t.anchura=self.anchura+puerta2.anchura
		if(self.grosor<puerta2.grosor):
			t.grosor=puerta2.grosor
		else:
			t.grosor=self.grosor
		t.color=self.color
		t.nbisagra=self.nbisagra+puerta2.nbisagra
		return t

a=puerta(10,10,3,5,"verde")
a.abrir()
b=puerta(30,20,2,8,"rojo")
c=a+b
c.muestra()
