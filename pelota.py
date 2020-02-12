#!/usr/bin/env python
# -*- coding: utf-8 -*-
#AGREGAR 3 PELOTAS + DETECTAR SI LA PALETA COLISIONO Y SI COLISIONO OBJETO OBJETO (PELOTA. PELOTA)
#GRABAR EN USUARIO|FECHA|COLISIONES|COORDENADAS
#SACAR INVORME POR FECHA. POR USUARIO, POR CORDENADAS POR COLISIONES:
#LAS COLISIONES PUEDEN SER DE DOS O MAS OBJETOS

# Módulos
import pygame
from pygame.locals import *
import sys
import time
# Constantes
WIDTH = 640
HEIGHT = 480
white = (255,255,255)   #constante para definir color blanco

# Clases
# ---------------------------------------------------------------------
class Text(pygame.font.Font):
    def __init__(self, FontName = None, FontSize = 30):
        pygame.font.init()
        self.font = pygame.font.Font(FontName, FontSize)
        self.size = FontSize

    def render(self, surface, text, color, pos):
        text = unicode(text, "UTF-8")
        x, y = pos
        for i in text.split("r"):
            surface.blit(self.font.render(i , 1, color),(x, y))
            y += self.size

class Disparo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen('images/ball.png', True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 10
        self.speed = 0.5
        self.choque = 0

    def disparar(self, time):
        if self.rect.centery > 0:
            self.rect.centery -= self.speed * time  #mueve hacia arrib -=
        if self.rect.centery <= 0:
            self.rect.centery = HEIGHT - 10



class Bola(pygame.sprite.Sprite):	#creo una clase que hereda todos los metodos de la clase pygame.sprite.Sprites

    def __init__(self, num, x, y):		#es la inicializacion de la Clase
        pygame.sprite.Sprite.__init__(self)	#invoco el metodo init de la clase heredada
        self.image = cargar_imagen('images/ball.png', True)	#uso la funcion para cargar la imagen
        self.rect = self.image.get_rect()	#tira la posicion y dimension de la imagen (probar imprimir)
        self.rect.centerx = x			#Inicia en la posicion central de la pantalla
        self.rect.centery = y
        self.speed =  [0.5, -0.5]	#define la velocidad de la pelota
        self.colision = 0
        self.num = num    #numero de pelota
        self.choque = 0

    def actualizar(self, time, pala_jug, pala_pc, puntos, choques, cod_usuario, fecha, pelota, pelota2, pelota3, bala):     #time parametro tiempo transcurrido

        self.rect.centerx += self.speed[0] * time   #uso la velocidad y tiempo para calcular la ubicacion
        self.rect.centery += self.speed[1] * time

        if self.rect.left <= 0:         #contador puntos PC
            puntos[0] += 1
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
            self.speed = [-0.5, 0.5]

        if self.rect.right >= WIDTH:                #contador puntos PLAYER
            puntos[1] += 1
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
            self.speed = [-0.5, 0.5]

        if self.rect.left <= 0 or self.rect.right >= WIDTH:     #si es menor a cero por izquierda o si por derecha es mayor a 640 rebota
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:    #para que no se pase arriba o abajo
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
            #pala player = pl
            #pala pc= pc
            #usuario|fecha|numpelota|paleta|corx|cordy
        if pygame.sprite.collide_rect(self, pala_jug):      # !!!FUNCION PARA SABER SI HUBO COLISION !! PLAYER
            self.speed[0] = -self.speed[0]                  #       Esto hace que rebote
            self.rect.centerx += self.speed[0] * time       #       Esto hace que rebote
            self.colision +=1   # colision player
            guardar(cod_usuario, fecha, self.num, "pl", self.rect.centerx, self.rect.centery)
        if pygame.sprite.collide_rect(self, pala_pc):      #!! FUNCIOON PARA SABER SI HUBO COLISION !! PC
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time       # hace que rebote
            guardar(cod_usuario, fecha, self.num, "pc", self.rect.centerx, self.rect.centery)
        if pygame.sprite.collide_rect(self, bala):
            choques[0] += 1
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            guardar(cod_usuario, fecha, self.num, "bala", self.rect.centerx, self.rect.centery)
        if self.num == 1:
            if pygame.sprite.collide_rect(self, pelota):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 2, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota2):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 3, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota3):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 4, self.rect.centerx, self.rect.centery)
        if self.num == 2:
            if pygame.sprite.collide_rect(self, pelota):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 1, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota2):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 3, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota3):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 4, self.rect.centerx, self.rect.centery)
        if self.num == 3:
            if pygame.sprite.collide_rect(self, pelota):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 1, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota2):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 2, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota3):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 4, self.rect.centerx, self.rect.centery)
        if self.num == 4:
            if pygame.sprite.collide_rect(self, pelota):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 1, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota2):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 2, self.rect.centerx, self.rect.centery)
            if pygame.sprite.collide_rect(self, pelota3):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
                guardar(cod_usuario, fecha, self.num, 3, self.rect.centerx, self.rect.centery)
        return puntos, choques



class Arma2(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen('images/pala.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 10
        self.speed = 0.5


class Pala(pygame.sprite.Sprite):

    def __init__(self, x):  #cuando creo un objeto de clase pala le paso x por parametro ej: pala_jug = Pala(30)
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen('images/pala.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2  #pa q arranque en el medio
        self.speed = 0.5

    def mover(self, time, keys):       #funcion para mover la paleta
        if self.rect.top >= 0:  #para que no desaparezca por la parte de arriba
            if keys[K_UP]:  #si preciono la flechita arriba
                self.rect.centery -= self.speed * time  #mueve pa arrib
        if self.rect.bottom <= HEIGHT:  #para que no se pase lo alto que definí
            if keys[K_DOWN]:    #si apreto flechita abajo
                self.rect.centery += self.speed * time  #muevo pabajo

    def ia(self, time, pelota):       #funcion inteligencia artificial para que se mueva sola la pc
        if pelota.speed[0] >= 0 and pelota.rect.centerx >= WIDTH / 2:   #bals.speed[0] > 0 cero, osea que la velocidad sea positiva, que este yendo a la derecha, y que haya pasado el centro de la pantalla
            if self.rect.centery < pelota.rect.centery:
                self.rect.centery += self.speed * time  #mueve hacia abajo +=
            if self.rect.centery > pelota.rect.centery:
                self.rect.centery -= self.speed * time  #mueve hacia arrib -=

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def guardar(cod_usuario, fecha, obj1, obj2, ejex, ejey):
    choque = open('colision.txt','a')
    registro = "{0},{1},{2},{3},{4},{5}\n".format(cod_usuario, fecha, obj1, obj2, ejex, ejey)
    choque.write(registro)
    choque.close()

def cargar_imagen(filename, transparent = False):
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message
	image = image.convert()	#convierte la imagen a formato interno de pygame
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image
# ---------------------------------------------------------------------

def main(cod_usuario, fecha):
    print cod_usuario
    text = Text()
    puntos = [0, 0]
    choques = [0, 0]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))   #creo la ventana
    pygame.display.set_caption("A VER SI ANDA ")    #Muestra arriba un texto

    imagen_fondo = cargar_imagen('images/fondo_pong.png')

    pelota = Bola(1, WIDTH / 2, HEIGHT / 2 )         #creo el objeto pelota
    pelota2 = Bola(2, 600, 250)
    pelota3 = Bola(3, 400, 300)
    pelota4 = Bola(4, 450, 315)
    pala_jug = Pala(30)     #le paso el parametro del eje x para que aparezca a 30 pix de lado izq y creo obj pala jugador
    pala_pc = Pala(WIDTH - 30)        #creo objeto paleta de la pc  width es 640 le resto 30 para q la pala quede en 610 del eje x
    arma = Arma2()
    bala = Disparo()
    clock = pygame.time.Clock()     #crea reloj para gestionar el tiempo

    jugando = True
    while jugando:                     # bucle principal
        time = clock.tick(60)   #framerate
        keys = pygame.key.get_pressed()  #verifica en el bucle si se esta presionadno alguna tecla
        for eventos in pygame.event.get():  #va controlando lo que sucede en el game. si apreta la x de salir cierra
            if eventos.type == QUIT:
                print pelota.colision   #muestro colisiones de pelota con paleta jugador
                jugando = False
        pelota.actualizar(time, pala_jug, pala_pc, puntos, choques, cod_usuario, fecha, pelota2, pelota3, pelota4, bala)     #Actualizo posicion pelota antes de mostrar en pantalla, le paso el obj paleta jugador
        pelota2.actualizar(time, pala_jug, pala_pc, puntos, choques, cod_usuario, fecha, pelota, pelota3, pelota4, bala)
        pelota3.actualizar(time, pala_jug, pala_pc, puntos, choques, cod_usuario, fecha, pelota, pelota2, pelota4, bala)
        pelota4.actualizar(time, pala_jug, pala_pc, puntos, choques, cod_usuario, fecha, pelota, pelota2, pelota3, bala)
        pala_jug.mover(time, keys)  #llamo al metodo mover, tiene que estar despues de actualizar la pelota
        pala_pc.ia(time, pelota)    #llamo al metodo inteligencia para que se mueva la paleta pc
        pala_pc.ia(time, pelota2)
        pala_pc.ia(time, pelota3)
        pala_pc.ia(time, pelota4)
        bala.disparar(time)
        screen.blit(imagen_fondo, (0, 0))   #cargo imagen de fondo en pantalla
        numero1 = str(puntos[1])
        text.render(screen, "P1: "+ numero1, white, (20, 0))
        numero0 = str(puntos[0])
        text.render(screen, "Cpu: "+ numero0, white, (560, 0))
        choque = str(choques[0])
        #text.render(screen, " choques "+ choque, white, (300, 0))
        text.render(screen,"Choque Disparo "+ choque, white, (300, 0))
        screen.blit(pelota.image, pelota.rect)  #cargo la pleota en pantalla
        screen.blit(pelota2.image, pelota2.rect)
        screen.blit(pelota3.image, pelota3.rect)
        screen.blit(pelota4.image, pelota4.rect)
        screen.blit(pala_jug.image, pala_jug.rect)  #cargo la paleta player
        screen.blit(pala_pc.image, pala_pc.rect)    #cargo paleta pc
        screen.blit(arma.image, arma.rect)
        screen.blit(bala.image, bala.rect)
        pygame.display.flip()   #actualiza la imagen
    # puntaje = open('mov.txt','a')
    # registro = "{0},{1},{2},{3},{4}\n".format(cod_usuario, fecha, pelota.colision , numero1, numero0)
    # puntaje.write(registro)
    #puntaje.close()
    pygame.quit()
