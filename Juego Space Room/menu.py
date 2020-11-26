# MODULOS
import pygame
import sys
import sqlite3
from locale import getdefaultlocale
import pandas as pd

class Menu:

    def __init__(self):

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("CREATE TABLE IF NOT EXISTS JUGADORES(id_jugador INTEGER PRIMARY KEY AUTOINCREMENT, nombre_jugador CHAR(10),nacionalidad CHAR(3),tiempo_jugador CHAR(10))")
        conexion.commit()  # hacemos commit para lanzarlo
        conexion.close()

        """ CREACION DE PANTALLA INICIAL
        ----------------------------------- """

        self.ventana_menu = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Menu de Juego")

        """ IMAGENES DE INICIO
               ------------------------- """
        # FONDO

        self.fondo_menu = pygame.image.load("./imagenes/libreta.jpg")
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (1920, 1080))
        self.ventana_menu.blit(self.fondo_menu, (0, 0))


        self.opcion_jugar_seleccionada = False
        self.opcion_ranking_seleccionada = False
        self.continuar = False



    def opciones(self):

        """ PUESTA EN MARCHA DEL JUEGO
        ---------------------------------"""

        # BUCLE HASTA FINALIZACION

        while not self.continuar:
            # OPCIONES

            # Tipo fuente Letras

            self.fuente = pygame.font.Font("./fuentes/PantonRustHeavy-GrSh.ttf", 60)

            if not self.opcion_jugar_seleccionada:

                self.opcion_jugar = self.fuente.render("JUGAR", 0, (0, 0, 0))
                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (550, 200))

            if not self.opcion_ranking_seleccionada:

                self.ranking = self.fuente.render("RANKING", 0, (0, 0, 0))
                self.ranking = self.ventana_menu.blit(self.ranking, (525, 300))

            for event in pygame.event.get():

                    # ACCION DE QUITAR PANTALLA CON (X) Y CON (ESC)

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()

                    # ACCION ON CLICK PARA GESTIONAR COLISIONES COMO SELECCION DE IMAGENES

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                        # RECOGEMOS LA POSICION X, Y DEL CLICK DEL RATON

                        x, y = pygame.mouse.get_pos()
                        # print("posicion "+str(pygame.mouse.get_pos()))

                        # COMPARACIONES COINCIDENCIAS CLICK RATON CON POSICIONES DE LOS OBJETOS IMAGEN

                        if self.opcion_jugar.collidepoint(x, y):

                            self.opcion_jugar_seleccionada = True

                            if self.opcion_jugar_seleccionada:

                                self.opcion_jugar = self.fuente.render("JUGAR", 0, (0, 0, 125))
                                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (550, 200))
                                self.ranking = self.fuente.render("RANKING", 0, (0, 0, 0))
                                self.ranking = self.ventana_menu.blit(self.ranking, (525, 300))
                                self.opcion_ranking_seleccionada = False


                            self.nick()

                            self.continuar = True

                        if self.ranking.collidepoint(x, y):

                            self.opcion_ranking_seleccionada = True

                            if self.opcion_ranking_seleccionada:

                                self.ranking = self.fuente.render("RANKING", 0, (0, 0, 125))
                                self.ranking = self.ventana_menu.blit(self.ranking, (525, 300))
                                self.opcion_jugar = self.fuente.render("JUGAR", 0, (0, 0, 0))
                                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (550, 200))
                                self.opcion_jugar_seleccionada = False

                            self.listado_ranking()

            pygame.display.flip()

    def nick(self):

        pygame.time.wait(500)

        self.nick_elegido = False

        self.nombre = ""

        self.posicion_x = 1170

        while not self.nick_elegido:

            self.ventana_menu.blit(self.fondo_menu, (0, 0))

            if self.opcion_jugar_seleccionada:
                self.opcion_jugar = self.fuente.render("JUGAR", 0, (0, 0, 125))
                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (550, 200))

            if not self.opcion_ranking_seleccionada:
                self.ranking = self.fuente.render("RANKING", 0, (0, 0, 0))
                self.ranking = self.ventana_menu.blit(self.ranking, (525, 300))

            self.mi_nick = self.fuente.render("NICK", 0, (0, 0, 0))
            self.mi_nick = self.ventana_menu.blit(self.mi_nick, (1185, 350))

            self.mi_nick_elegido = pygame.font.Font("./fuentes/ABCThru.ttf", 45)
            self.mi_nick_elegido.set_bold(True)
            self.mi_nick_elegido = self.mi_nick_elegido.render(self.nombre, 0, (0, 0, 0))
            self.mi_nick_elegido = self.ventana_menu.blit(self.mi_nick_elegido, (self.posicion_x, 465))

            self.confirmar = pygame.image.load("./imagenes/confirmar.png")
            self.confirmar = pygame.transform.scale(self.confirmar, (50, 50))
            self.confirmar = self.ventana_menu.blit(self.confirmar, (1275, 550))

            self.anular = pygame.image.load("./imagenes/anular.png")
            self.anular = pygame.transform.scale(self.anular, (50, 50))
            self.anular = self.ventana_menu.blit(self.anular, (1175, 550))

            for event in pygame.event.get():

                # ACCION DE QUITAR PANTALLA CON (X) Y CON (ESC)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # si alguna tecla es presionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

                    if len(self.nombre) < 10:

                        try:
                            # obtiene el nombre de la tecla
                            self.key_name = pygame.key.name(event.key)

                            # imprime en la consola la tecla presionada
                            print(u'Tecla "{}" presionada'.format(self.key_name))
                            print(self.nombre)
                            print(len(self.nombre))

                            print("The ASCII value of '" + self.key_name + "' is", ord(self.key_name))

                            # convierte el nombre de la tecla en mayúsculas
                            self.key_name = self.key_name.upper()

                            print("The ASCII value of '" + self.key_name + "' is", ord(self.key_name))

                            if 33 <= ord(self.key_name) <= 126:

                                self.nombre += str(self.key_name)

                                self.posicion_x -= 6

                            else:
                                self.nombre = self.nombre

                        except (TypeError):
                            pass

                    else:
                        pass

                # ACCION ON CLICK PARA GESTIONAR COLISIONES COMO SELECCION DE IMAGENES

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    # RECOGEMOS LA POSICION X, Y DEL CLICK DEL RATON

                    x, y = pygame.mouse.get_pos()
                    # print("posicion "+str(pygame.mouse.get_pos()))

                    # COMPARACIONES COINCIDENCIAS CLICK RATON CON POSICIONES DE LOS OBJETOS IMAGEN

                    if self.anular.collidepoint(x, y):

                        self.nombre = ""
                        self.posicion_x = 1170

                    if self.confirmar.collidepoint(x, y):

                        conexion = sqlite3.connect('escapeRoom.db')
                        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
                        if self.nombre == "":
                            self.nombre = "**********"

                        lenguaje, encoding = getdefaultlocale()
                        print(lenguaje[3:])
                        self.idioma = lenguaje[3:]
                        cursor.execute("INSERT INTO JUGADORES (nombre_jugador, nacionalidad) VALUES('" + self.nombre + "','" + self.idioma + "')")
                        conexion.commit()  # hacemos commit para lanzarlo
                        conexion.close()

                        self.nick_elegido = True

            pygame.display.flip()

    def listado_ranking(self):

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT nombre_jugador FROM JUGADORES WHERE id_jugador < 11")
        self.datos_jugadores = cursor.fetchall()  # guarda el primer registro y envia una tupla

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT nacionalidad FROM JUGADORES WHERE id_jugador < 11")
        self.nacion_jugadores = cursor.fetchall()  # guarda el primer registro y envia una tupla

        self.posicion_y = 190
        self.posicion_y2 = 190

        self.dic_jugadores = {}

        for self.datos_jugador in self.datos_jugadores:

            self.dic_jugadores = {'nombre': self.datos_jugador,'nacion': self.nacion_jugadores}

            self.mi_nick_elegido = pygame.font.Font("./fuentes/ABCThru.ttf", 30)
            self.mi_nick_elegido.set_bold(True)
            self.mi_nick_elegido = self.mi_nick_elegido.render(self.dic_jugadores['nombre'][0], 0, (0, 0, 0))
            self.mi_nick_elegido = self.ventana_menu.blit(self.mi_nick_elegido, (1100, self.posicion_y))

            self.posicion_y += 60

        for self.nacion_jugador in self.nacion_jugadores:
            self.dic_jugadores = {'nombre': self.datos_jugador, 'nacion': self.nacion_jugador}

            print(self.dic_jugadores['nombre'][0], self.dic_jugadores['nacion'][0])
            print(self.dic_jugadores['nacion'][0])
            '''df = pd.read_csv('./GeoLite2-Country-Locations-en.csv')
            self.pais_jugador = self.dic_jugadores['nacion'][0]
            print(self.pais_jugador)
            self.pais_bandera = df[(df.country_iso_code== self.pais_jugador)].country_name
            print(self.pais_bandera)
            print("./imagenes/banderas/'"+self.pais_bandera+"'.png")'''
            self.bandera_mostrada = pygame.image.load("./imagenes/banderas/"+self.dic_jugadores['nacion'][0]+".png")
            #self.bandera_mostrada = pygame.image.load("./imagenes/banderas/Spain.png"[2:])
            self.bandera_mostrada = pygame.transform.scale(self.bandera_mostrada, (40, 30))
            self.bandera_mostrada = self.ventana_menu.blit(self.bandera_mostrada, (1400, self.posicion_y2))

            self.posicion_y2 += 60

        conexion.close()