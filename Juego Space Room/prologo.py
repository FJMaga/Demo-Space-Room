import sqlite3

import pygame
import  sys

class Prologo:

    def __init__(self):

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT nombre_jugador FROM JUGADORES order by id_jugador DESC limit 1")
        self.nombre = cursor.fetchone()
        # print(self.nombre[0])
        conexion.commit()  # hacemos commit para lanzarlo
        conexion.close()

        """ CREACION DE PANTALLA INICIAL
                ----------------------------------- """

        self.ventana_menu = pygame.display.set_mode((1480, 800))
        pygame.display.set_caption("Menu de Juego")

        """ IMAGENES DE INICIO
               ------------------------- """
        # FONDO

        self.fondo_menu = pygame.image.load("./imagenes/ventana_tierra.jpg")
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (1480, 800))
        self.ventana_menu.blit(self.fondo_menu, (0, 0))

        self.pantalla_escritura = pygame.image.load("./imagenes/mundo/1.png")
        self.pantalla_escritura = pygame.transform.scale(self.pantalla_escritura, (552, 330))
        self.ventana_menu.blit(self.pantalla_escritura, (475, 0))

        self.pantalla_mundo = pygame.image.load("./imagenes/11.jpg")
        self.pantalla_mundo = pygame.transform.scale(self.pantalla_mundo, (852, 480))
        self.ventana_menu.blit(self.pantalla_mundo, (325, 325))

        self.llamada = True

        self.escrito_astronauta = ""
        self.escrito_astronauta2 = ""
        self.escrito_astronauta3 = ""
        self.escrito_astronauta4 = ""
        self.escrito_astronauta5 = ""

        self.i = 1
        self.i2 = 0
        self.i3 = 0
        self.i4 = 0
        self.i5 = 0
        self.i6 = 0
        self.i7 = 0
        self.i8 = 0
        self.i9 = 0
        self.i10 = 0

        self.cont = 0

        self.conversacion1 = False
        self.respuesta_conversacion1 = False
        self.continuar1 = False
        self.conversacion2 = False
        self.respuesta_conversacion2 = False
        self.continuar2 = False
        self.conversacion3 = False
        self.respuesta_conversacion3 = False



    def pantallas(self):

        while self.llamada:

            for event in pygame.event.get():

                    # ACCION DE QUITAR PANTALLA CON (X) Y CON (ESC)

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()

            self.pantalla_mundo = pygame.image.load("./imagenes/mundo/"+str(self.i)+".png")
            self.pantalla_mundo = pygame.transform.scale(self.pantalla_mundo, (552, 330))
            self.ventana_menu.blit(self.pantalla_mundo, (475, 0))

            self.pantalla_escritura = pygame.image.load("./imagenes/11.jpg")
            self.pantalla_escritura = pygame.transform.scale(self.pantalla_escritura, (852, 480))
            self.ventana_menu.blit(self.pantalla_escritura, (325, 325))

            self.dialogo()

            if self.i == 111:
                self.i = 1
            else:
                self.i += 1

            pygame.time.wait(50)

            pygame.display.flip()




    def dialogo(self):

        if not self.conversacion1 and not self.conversacion2:

            self.escrito_astronauta += 'Astronauta ES-253 a base, contesten, por favor'[self.i2]

            self.texto1 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
            self.texto1 = self.texto1.render(self.escrito_astronauta, 0, (255, 255, 255))
            self.texto1 = self.ventana_menu.blit(self.texto1, (520, 430))

        else:

            self.texto1 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
            self.texto1 = self.texto1.render('Astronauta ES-253 a base, contesten, por favor', 0, (255, 255, 255))
            self.texto1 = self.ventana_menu.blit(self.texto1, (520, 430))




        #print('longitud palabra',len('Astronauta ES-253 a base, contesten, por favor'))

        #print(self.i2)

        if self.i2 == len('Astronauta ES-253 a base, contesten, por favor')-1:
            #self.escrito_astronauta=""
            #self.i2=0
            #self.cont+=1
            self.conversacion1 = True
            #print(self.i2)

        if self.i2 == len('Astronauta ES-253 a base, contesten, por favor')+5:
            #pygame.time.wait(1000)
            self.respuesta_conversacion1 = True


        if self.respuesta_conversacion1:

            self.respuesta_texto1 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
            self.respuesta_texto1 = self.respuesta_texto1.render("Radio aficionado '" + self.nombre[0] + "', le copio", 0, (0, 150, 255))
            self.respuesta_texto1 = self.ventana_menu.blit(self.respuesta_texto1, (520, 450))

        if self.i2 == len('Astronauta ES-253 a base, contesten, por favor') + 10:
            self.continuar1 = True

        self.i2 += 1


        # INICIO CONVERSACION 2

        if self.conversacion1 and not self.conversacion2 and self.respuesta_conversacion1 and self.continuar1:

            if self.i3 <= 52:
                self.escrito_astronauta2 += \
                'la nave se encuentra a la deriva y estamos encerrados,'[self.i3]
                self.texto2 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.texto2 = self.texto2.render(self.escrito_astronauta2, 0, (255, 255, 255))
                self.texto2 = self.ventana_menu.blit(self.texto2, (520, 470))

            else:
                self.escrito_astronauta3 += 'necesitamos llegar a la navegación, sino chocaremos '[self.i4]

                self.texto3 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.texto3 = self.texto3.render(self.escrito_astronauta3, 0, (255, 255, 255))
                self.texto3 = self.ventana_menu.blit(self.texto3, (520, 490))

                self.i4 += 1



            self.i3 += 1


        #print(self.i3)

        if self.i3 >= len('la nave se encuentra a la deriva y estamos encerrados,'):
            # self.escrito_astronauta=""
            # self.i2=0
            self.texto2 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
            self.texto2 = self.texto2.render('la nave se encuentra a la deriva y estamos encerrados', 0,(255, 255, 255))
            self.texto2 = self.ventana_menu.blit(self.texto2, (520, 470))
            #print(self.i3)

        if self.i4 >= len('necesitamos llegar a la navegación, sino chocaremos '):
            # self.escrito_astronauta=""
            # self.i2=0
            self.texto3 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
            self.texto3 = self.texto3.render(self.escrito_astronauta3, 0, (255, 255, 255))
            self.texto3 = self.ventana_menu.blit(self.texto3, (520, 490))

            self.conversacion2 = True
            self.i4 += 1
            #print(self.i4)

        if self.i4 == len('necesitamos llegar a la navegación, sino chocaremos ')+5:
            #pygame.time.wait(1000)
            self.respuesta_conversacion2 = True

        if self.respuesta_conversacion2:
            self.respuesta_texto2 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
            self.respuesta_texto2 = self.respuesta_texto2.render('como puedo ayudaros?', 0, (0, 150, 255))
            self.respuesta_texto2 = self.ventana_menu.blit(self.respuesta_texto2, (520, 510))

        if self.i4 == len('necesitamos llegar a la navegación, sino chocaremos ') + 10:
            # pygame.time.wait(1000)
            self.continuar2 = True

        # INICIO CONVERSACION 3

        if self.conversacion2 and not self.conversacion3 and self.respuesta_conversacion2 and self.continuar2:

            if self.i5 <= 40:
                self.escrito_astronauta4 += \
                    'la única forma es que controles un cyborg '[self.i5]
                self.texto4 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.texto4 = self.texto4.render(self.escrito_astronauta4, 0, (255, 255, 255))
                self.texto4 = self.ventana_menu.blit(self.texto4, (520, 530))

            else:
                self.escrito_astronauta5 += 'estamos en tus manos, tienes 60 minutos, SUERTE  '[self.i6]

                self.texto5 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.texto5 = self.texto5.render(self.escrito_astronauta5, 0, (255, 255, 255))
                self.texto5 = self.ventana_menu.blit(self.texto5, (520, 550))

                if self.i6 < 48:
                    self.i6 += 1

                #print(self.i6)
                #print('longitud' + str(len('estamos en tus manos, tienes 60 minutos, SUERTE ')))

            self.i5 += 1

            #print(self.i5)

            if self.i5 >= len('la única forma es que controles un cyborg '):
                # self.escrito_astronauta=""
                # self.i2=0
                self.texto4 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.texto4 = self.texto4.render('la única forma es que controles un cyborg ', 0,
                                                 (255, 255, 255))
                self.texto4 = self.ventana_menu.blit(self.texto4, (520, 530))
                #print(self.i5)

            if self.i6 >= len('estamos en tus manos, tienes 60 minutos, SUERTE '):
                # self.escrito_astronauta=""
                # self.i2=0
                self.texto5 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.texto5 = self.texto5.render(self.escrito_astronauta5, 0, (255, 255, 255))
                self.texto5 = self.ventana_menu.blit(self.texto5, (520, 550))

                self.conversacion2 = True
                self.i7 += 1

                #print(self.i6)

            if self.i7 >= 5:
                # pygame.time.wait(1000)

                self.respuesta_texto3 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.respuesta_texto3 = self.respuesta_texto3.render('pero... yo no tengo conocimientos de aeronáutica...', 0, (0, 150, 255))
                self.respuesta_texto3 = self.ventana_menu.blit(self.respuesta_texto3, (520, 570))

                self.i8 += 1

            if self.i8 >= 15:
                # pygame.time.wait(1000)
                self.respuesta_texto4 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.respuesta_texto4 = self.respuesta_texto4.render(
                    'hola... sigues ahí...', 0, (0, 150, 255))
                self.respuesta_texto4 = self.ventana_menu.blit(self.respuesta_texto4, (520, 590))

                self.i9 += 1

            if self.i9 >= 15:
                # pygame.time.wait(1000)
                self.respuesta_texto5 = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
                self.respuesta_texto5 = self.respuesta_texto5.render(
                    'no os preocupéis, os sacaré de esta !', 0, (0, 150, 255))
                self.respuesta_texto5 = self.ventana_menu.blit(self.respuesta_texto5, (520, 610))

                self.i10 += 1

            if self.i10 >= 15:
                self.llamada = False