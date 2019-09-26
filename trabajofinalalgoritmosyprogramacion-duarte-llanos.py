import random,time
import os, sys
import pygame
from pygame.locals import *	


class Inicio():#clase que inicia el juego
	
	def __init__(self):
		puntaje=Intentos()
		nuevo = Pantalla(puntaje)
		
class CargaDeDatos():#carga los datos provenientes de los archivos txt asociados a las categorias
	def __init__(self, categoria):#se cargan las categorias 
		self.__categoria = categoria#las preguntas y respuestas se cargan a estas listas
		self.__preguntas = []
		self.__respuestascorrectas= []
		self.__respuestasincorrectas= []
		self.__respuestasincorrectas2=[]
		

	def cargarPreguntas(self):#dependiendo cual categoria se ha seleccionado con el mouse se cargaran las preguntas de los archivos de texto indicados
		if self.__categoria == "Geografia":
			pregun = open ("preguntasgeografia.txt", "r")
		elif self.__categoria == "Historia":
			pregun = open ("preguntashistoria.txt", "r")
		elif self.__categoria == "Matematica":
			pregun= open ("preguntasmatematica.txt", "r")
			
		lineas = pregun.read()#con este comando se abre el archivo y lee el texto
		pregun.close
		lineas = lineas.split(",")#con split separamos los datos que aparecen en ese texto
		for li in lineas:#con este bucle guardamos las preguntas en la lista self.__preguntas
			self.__preguntas.append(li)
		
		
	def cargarRespuestasCorrectas(self):#se cargan las respuestas correctas de las preguntas de esa categoria
		if self.__categoria == "Geografia":
			rescor = open ("respuestascorrectasgeografia.txt", "r")
		elif self.__categoria == "Historia":
			rescor= open ("respuestascorrectashistoria.txt", "r")
		elif self.__categoria == "Matematica":
			rescor= open ("respuestascorrectasmatematica.txt", "r")
		
		lineas=rescor.read()
		rescor.close
		lineas=lineas.split(",")
		for li in lineas:#guardamos las respuestas correctas en self.__respuestascorrectas
			self.__respuestascorrectas.append(li)
		
			
	def cargarRespuestasIncorrectas(self):#se cargan las respuestas incorrectas para las preguntas de esa categoria	
		if self.__categoria == "Geografia":
			resinc= open ("respuestasincorrectasgeografia.txt", "r")
		elif self.__categoria == "Historia":
			resinc= open ("respuestasincorrectashistoria.txt", "r")
		elif self.__categoria == "Matematica":
			resinc= open ("respuestasincorrectasmatematica.txt", "r")
		lineas = resinc.read()
		resinc.close
		lineas = lineas.split(",")
		for li in lineas:#guardamos las respuestas incorrectas en self.__respuestasincorrectas
			self.__respuestasincorrectas.append(li)
	
	def cargarRespuestasIncorrectas2(self):#se cargan las respuestas incorrectas para las preguntas de esa categoria	
		if self.__categoria == "Geografia":
			resinc2= open ("respuestasincorrectasgeografia2.txt", "r")
		elif self.__categoria == "Historia":
			resinc2= open ("respuestasincorrectas2historia.txt", "r")
		elif self.__categoria == "Matematica":
			resinc2= open ("respuestasincorrectasmatematica2.txt", "r")
		lineas = resinc2.read()
		resinc2.close
		lineas = lineas.split(",")
		for li in lineas:#guardamos las respuestas incorrectas en self.__respuestasincorrectas
			self.__respuestasincorrectas2.append(li)				
		
	def obtenerPregunta(self, posicion):#devuelve la pregunta en esa posicion
		return self.__preguntas[posicion]
		
	def obtenerRespuestaCorrecta(self,posicion):#devuelve la respuesta correcta en esa posicion
		return self.__respuestascorrectas[posicion]	
		
	
	def obtenerRespuestaIncorrecta(self,posicion):#devuelve la respuesta incorrecta en esa posicion
		return self.__respuestasincorrectas[posicion]
	
	def obtenerRespuestaIncorrecta2(self,posicion):#devuelve la respuesta incorrecta en esa posicion
		return self.__respuestasincorrectas2[posicion]			
		
class Pantalla(Inicio):#Se carga la pantalla principal
	
	def __init__(self, puntaje):
		self.__puntaje = puntaje
		self.ventana = pygame.display.set_mode((1000,520))
		pygame.display.set_caption("cuanto sabes")
		self.__ventanalimpia = self.ventana.copy() 
		while True:
			eventos=pygame.event.get()
			for evento in eventos:
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
					
			fondito=pygame.image.load("fondopan2.jpg")
			self.ventana.blit(fondito, (0,0))
			pygame.display.flip()
			self.presiona()
			while True:	
				if not (pygame.mouse.get_pos()[0]>=800 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[0]<=959 and pygame.mouse.get_pos()[1]<=294 or  pygame.mouse.get_pos()[0]>=800 and pygame.mouse.get_pos()[1]>=300 and pygame.mouse.get_pos()[0]<=959 and pygame.mouse.get_pos()[1]<=373):
					self.presiona()
				else:	
					if pygame.mouse.get_pos()[0]>=800 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[0]<=959 and pygame.mouse.get_pos()[1]<=294:		
						self.pantallaTematica(self.__puntaje)	
			
					elif pygame.mouse.get_pos()[0]>=800 and pygame.mouse.get_pos()[1]>=300 and pygame.mouse.get_pos()[0]<=959 and pygame.mouse.get_pos()[1]<=373:	
						pygame.quit()
						sys.exit()
	def pantallaTematica(self, puntaje):#carga la pantalla con las imagenes  de las categorias
		 
		fondoini= pygame.image.load("categoria.jpg")
		self.ventana.blit(fondoini, (0,0))
		pygame.display.update()	
		self.presiona()
		if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[0] <= 350 and  pygame.mouse.get_pos()[1] <= 500:#si apreta en esta posicion se abrira el nivel de las preguntas de geografia
			categoria = "Geografia"
			gestor=ManejoJuego(self.__puntaje)
			gestor.crear(categoria)
		elif pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 500 and  pygame.mouse.get_pos()[1] <= 520:#si apreta en esta posicion se abrira el nivel de las preguntas de historia
			categoria = "Historia"
			gestor= ManejoJuego(self.__puntaje)
			gestor.crear(categoria)
		elif pygame.mouse.get_pos()[0] >= 550 and pygame.mouse.get_pos()[1] >= 450 and pygame.mouse.get_pos()[0] <= 750 and  pygame.mouse.get_pos()[1] <= 500:#si apreta en esta posicion se abrira el nivel de las preguntas de matematica
			categoria = "Matematica"
			gestor= ManejoJuego(self.__puntaje)
			gestor.crear(categoria)

	def presiona(self):#lee la posicion del mouse
				
		while True:
			for event in pygame.event.get():#si se presiona la x se cierra el juego
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				else:	
					if event.type==MOUSEBUTTONDOWN:#devuelve la posicion del mouse
						x_posicion, y_posicion = pygame.mouse.get_pos()  
						return x_posicion, y_posicion



					
class ManejoJuego(Pantalla):#
	def __init__(self, puntaje):
		self.__puntaje=puntaje
				
	def crear(self, categoria):
		print self.__puntaje
		nivel=CargaDeDatos(categoria)
		nivel.cargarPreguntas()
		nivel.cargarRespuestasCorrectas()
		nivel.cargarRespuestasIncorrectas()
		nivel.cargarRespuestasIncorrectas2()
		for i in range(0,10):
			comenzar= PantallaDeJuego(nivel.obtenerPregunta(i), nivel.obtenerRespuestaCorrecta(i), nivel.obtenerRespuestaIncorrecta(i),nivel.obtenerRespuestaIncorrecta2(i),self.__puntaje)#llama a la pantalla de juego
		self.__puntaje.muestrapuntaje() 		

									
class PantallaDeJuego(Pantalla):#carga la pantalla de fondo del juego	
	def __init__(self, pregunta, respuestacorrecta, respuestaincorrecta,respuestaincorrecta2,puntaje):
		self.__puntaje= puntaje
		self.__pregunta = pregunta
		self.__respuestacorrecta = respuestacorrecta
		self.__respuestaincorrecta = respuestaincorrecta
		self.__respuestaincorrecta2 = respuestaincorrecta2
		self.ventana = pygame.display.set_mode((1000,520))
		pygame.display.set_caption("Cuanto sabes")
		self.__pantallavacia = self.ventana.copy() 
		self.ventana.blit(self.__pantallavacia,(0,0))
		pygame.display.update()
		self.formar()#llama a la funcion formar
	
	def cambiar_posicion(self):#cambia de posicion las preguntas
		lista=[220,320,420]
		random.shuffle(lista)
		return lista
					
	def formar(self):#muestra en pantalla las preguntas y respuestas
		fondopregun = pygame.image.load("pantalladejuego.jpg")
		self.ventana.blit(fondopregun, (0,0))
		self.ventana.blit(fondopregun, (0,0))
		pygame.display.update()
		time.sleep(0.5)
		fuente1 = pygame.font.SysFont("Arial", 40)
		fuente2 = pygame.font.SysFont("Arial", 60)
		preguntaimagen = fuente1.render(self.__pregunta, True,(128,0,255))
		respuestaimagen = fuente2.render(self.__respuestacorrecta, True,(128,0,255))
		respuestaincorrectaimagen = fuente2.render(self.__respuestaincorrecta, True,(128,0,255))
		respuestaincorrectaimagen2 = fuente2.render(self.__respuestaincorrecta2, True,(128,0,255))
		self.ventana.blit(preguntaimagen, (270,20))
		pygame.display.update()
		time.sleep(0.2)
		poslist = self.cambiar_posicion() 
		self.ventana.blit(respuestaimagen,(405,poslist[0]))
		pygame.display.update()
		time.sleep(0.2)
		self.ventana.blit(respuestaincorrectaimagen,(405,poslist[1]))
		pygame.display.update()
		time.sleep(0.2)
		self.ventana.blit(respuestaincorrectaimagen2,(405,poslist[2]))
		pygame.display.update()
		time.sleep(0.2)
		self.presiona()		
		
		while True:#esto permite reconocer siempre la respuesta elegida en pantalla
			if not (pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[0]<=990 and  pygame.mouse.get_pos()[1]<=300 or pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[1]>=304 and pygame.mouse.get_pos()[0]<=990 and  pygame.mouse.get_pos()[1]<=394 or pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[1]>=400 and pygame.mouse.get_pos()[0]<=990 and  pygame.mouse.get_pos()[1]<=500):
				self.presiona()
			else:
				if pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[0]<=990 and  pygame.mouse.get_pos()[1]<=300:		
					if poslist[0]==220:	
						self.__puntaje.sumarCorrectas()
					else:
						self.__puntaje.sumarIncorrectas()
				elif  pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[1]>=304 and pygame.mouse.get_pos()[0]<=990 and  pygame.mouse.get_pos()[1]<=394:
					if poslist[0]==320:
						self.__puntaje.sumarCorrectas()
					else:
						self.__puntaje.sumarIncorrectas()
				elif pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[1]>=400 and pygame.mouse.get_pos()[0]<=990 and  pygame.mouse.get_pos()[1]<=500:
					if poslist[0]==420:
						self.__puntaje.sumarCorrectas()
					else:
						self.__puntaje.sumarIncorrectas()			
				break#esto evita que se cree un bucle infinito dentro del juego	
		correcto= pygame.image.load("bien.jpg")
		incorrecto= pygame.image.load("mal.jpg")
		self.ventana.blit(correcto,(900,poslist[0]))
		pygame.display.update()
		time.sleep(0.2)
		self.ventana.blit(incorrecto,(900,poslist[1]))
		pygame.display.update()
		time.sleep(0.2)
		self.ventana.blit(incorrecto,(900,poslist[2]))
		pygame.display.update()
		time.sleep(0.2)
		

class Intentos(Pantalla):	
	def __init__(self):
		self.__correctas = 0
		self.__incorrectas = 0
		self.ventana = pygame.display.set_mode((1000,520))
		pygame.display.set_caption("Cuanto sabes")
		self.__ventanalimpia = self.ventana.copy() 
		self.ventana.blit(self.__ventanalimpia,(0,0))
		pygame.display.update()
		
	def __str__(self):
		cadena=str(self.__correctas) + ',' + str(self.__incorrectas)
		return cadena
		                                                                                                                                                                                                                                             					
	def resetIntentos(self):
		self.__correctas = 0
		self.__incorrectas = 0
		
	def sumarCorrectas(self):
		self.__correctas = self.__correctas + 1
	
	def sumarIncorrectas(self):
		self.__incorrectas =  self.__incorrectas + 1
		
	def totalIncorrectas(self):
		return self.__incorrectas
				 
	def totalCorrectas(self):	
		return self.__correctas	
		
	def muestrapuntaje(self):
		pantallafinal= pygame.image.load("fondo28.jpg")
		self.ventana.blit(pantallafinal, (0,0))
		pygame.display.update()
		time.sleep(1.5)
		fuente3 = pygame.font.SysFont("Arial", 90)
		mostras= str(self.totalCorrectas())
		muestra = fuente3.render((mostras), True,(0,0,0))
		self.ventana.blit(muestra, (250,180))
		pygame.display.update()
		time.sleep(0.5)
		incorrectas= self.totalIncorrectas()
		muestraincorrecta= fuente3.render(str(incorrectas), True,(0,0,0))
		self.ventana.blit(muestraincorrecta, (250,400))
		mostras = 0
		muestraincorrecta = 0
		self.resetIntentos()
		pygame.display.update()
		time.sleep(0.5)
	
		
	

pygame.init()
ejecutar = Inicio()




