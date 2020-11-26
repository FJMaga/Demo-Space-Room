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

        self.ventana_menu = pygame.display.set_mode((1480, 800))
        pygame.display.set_caption("Menu de Juego")

        """ IMAGENES DE INICIO
               ------------------------- """
        # FONDO

        self.fondo_menu = pygame.image.load("./imagenes/ventana_tierra.jpg")
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (1480, 800))
        self.ventana_menu.blit(self.fondo_menu, (0, 0))

        self.color_lineas_rectangulo = (55, 55, 55)
        self.color_linea = (75, 150, 200)
        self.rectangulo = pygame.draw.rect(self.ventana_menu, self.color_lineas_rectangulo, (450, 590, 600, 200), 1)

        self.opcion_jugar_seleccionada = False
        self.opcion_ranking_seleccionada = False
        self.opcion_instrucciones_seleccionada = False
        self.opcion_creditos_seleccionada = False

        # --------------------------------------------------------

        self.continuar = False
        self.sms = False

        self.salir_creditos = False
        self.mostrar_designer = True
        self.mostrar_creado = False
        self.mostrar_copyrght = False

        self.mostrar_instruccion_1 = True
        self.mostrar_instruccion_2 = False
        self.mostrar_instruccion_3 = False
        self.mostrar_instruccion_4 = False
        self.mostrar_instruccion_5 = False
        self.mostrar_instruccion_6 = False

        self.cont = 0

        # TIEMPO

        self.tiempo_transcurrido = 0

        self.rango1 = 0
        self.rango2 = 0

        # ------------------------------------------

        self.y = 0
        self.y2 = 0
        self.y3 = 0

        self.i = 0


    def opciones(self):

        """ PUESTA EN MARCHA DEL JUEGO
        ---------------------------------"""

        # BUCLE HASTA FINALIZACION

        while not self.continuar:

            if self.opcion_creditos_seleccionada:

                self.creditos()

            if self.opcion_instrucciones_seleccionada:

                self.instrucciones()
            else:
                self.i = 0

            # OPCIONES

            # Tipo fuente Letras

            self.fuente = pygame.font.Font("./fuentes/ABCThru.ttf", 30)

            if not self.opcion_jugar_seleccionada:

                self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

            if not self.opcion_ranking_seleccionada:

                self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
                self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

            if not self.opcion_instrucciones_seleccionada:

                self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
                self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones, (635, 700))

            if not self.opcion_creditos_seleccionada:

                self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
                self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

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
                                self.opcion_jugar = self.fuente.render("JUGAR", 0, (155, 155, 155))
                                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

                                self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
                                self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

                                self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
                                self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,(635, 700))

                                self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
                                self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

                                self.opcion_ranking_seleccionada = False
                                self.opcion_instrucciones_seleccionada = False
                                self.opcion_creditos_seleccionada = False

                            self.nick()

                            self.continuar = True

                        if self.ranking.collidepoint(x, y):

                            self.opcion_ranking_seleccionada = True

                            if self.opcion_ranking_seleccionada:

                                self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
                                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

                                self.ranking = self.fuente.render("RANKING", 0, (155, 155, 155))
                                self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

                                self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
                                self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,
                                                                                   (635, 700))

                                self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
                                self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

                                self.opcion_jugar_seleccionada = False
                                self.opcion_instrucciones_seleccionada = False
                                self.opcion_creditos_seleccionada = False


                            self.listado_ranking()

                        if self.opcion_instrucciones.collidepoint(x, y):

                            self.opcion_instrucciones_seleccionada = True

                            if self.opcion_instrucciones_seleccionada:

                                self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
                                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

                                self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
                                self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

                                self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (155, 155, 155))
                                self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,
                                                                                   (635, 700))

                                self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
                                self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

                                self.opcion_jugar_seleccionada = False
                                self.opcion_ranking_seleccionada = False
                                self.opcion_creditos_seleccionada = False


                        if self.opcion_creditos.collidepoint(x, y):

                            self.opcion_creditos_seleccionada = True

                            if self.opcion_creditos_seleccionada:

                                self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
                                self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

                                self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
                                self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

                                self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
                                self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,
                                                                                   (635, 700))

                                self.opcion_creditos = self.fuente.render("CREDITOS", 0, (155, 155, 155))
                                self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

                                self.opcion_jugar_seleccionada = False
                                self.opcion_ranking_seleccionada = False
                                self.opcion_instrucciones_seleccionada = False



            pygame.display.flip()

    def nick(self):

        pygame.time.wait(500)

        self.nick_elegido = False

        self.nombre = ""

        self.posicion_x = 715

        while not self.nick_elegido:

            self.resetear()

            self.mi_nick = self.fuente.render("NICK", 0, (255, 255, 255))
            self.mi_nick = self.ventana_menu.blit(self.mi_nick, (700, 425))

            self.mi_nick_elegido = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 25)
            #self.mi_nick_elegido.set_bold(True)
            self.mi_nick_elegido = self.mi_nick_elegido.render(self.nombre, 0, (255, 255, 255))
            self.mi_nick_elegido = self.ventana_menu.blit(self.mi_nick_elegido, (self.posicion_x, 475))
            #self.linea = pygame.draw.line(self.ventana_menu, self.color_linea, (625, 500), (850, 500), 3)

            self.confirmar = pygame.image.load("./imagenes/confirmar.png")
            self.confirmar = pygame.transform.scale(self.confirmar, (20, 20))
            self.confirmar = self.ventana_menu.blit(self.confirmar, (700, 525))

            self.anular = pygame.image.load("./imagenes/anular.png")
            self.anular = pygame.transform.scale(self.anular, (20, 20))
            self.anular = self.ventana_menu.blit(self.anular, (750, 525))

            if self.sms:
                self.mensaje = "No confio en alguien que no revela su nombre"
                self.mi_mensaje = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 20)
                self.mi_mensaje = self.mi_mensaje.render(self.mensaje, 0, (255, 0, 0))
                self.mi_mensaje = self.ventana_menu.blit(self.mi_mensaje, (475, 475))
                #self.linea = pygame.draw.line(self.ventana_menu, (255, 0, 0), (475, 500), (975, 500), 3)
            else:
                self.linea = pygame.draw.line(self.ventana_menu, self.color_linea, (625, 500), (850, 500), 3)

            for event in pygame.event.get():

                # ACCION DE QUITAR PANTALLA CON (X) Y CON (ESC)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # si alguna tecla es presionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        self.nombre = self.nombre[:len(self.nombre)-1]
                        self.posicion_x += 5
                    if event.key == pygame.K_SPACE:
                        self.nombre += " "
                        self.posicion_x -=5

                    if len(self.nombre) < 10:
                        try:
                            # obtiene el nombre de la tecla
                            self.key_name = pygame.key.name(event.key)

                            # imprime en la consola la tecla presionada
                            #print(u'Tecla "{}" presionada'.format(self.key_name))
                            #print(self.nombre)
                            #print(len(self.nombre))

                            #print("The ASCII value of '" + self.key_name + "' is", ord(self.key_name))

                            # convierte el nombre de la tecla en mayúsculas
                            self.key_name = self.key_name.upper()

                            #print("The ASCII value of '" + self.key_name + "' is", ord(self.key_name))

                            if 33 <= ord(self.key_name) <= 126:

                                self.nombre += str(self.key_name)

                                self.posicion_x -= 5

                            else:
                                self.nombre = self.nombre


                        except (TypeError):
                            pass

                        self.sms = False

                    else:
                        pass


                # ACCION ON CLICK PARA GESTIONAR COLISIONES COMO SELECCION DE IMAGENES

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    # RECOGEMOS LA POSICION X, Y DEL CLICK DEL RATON

                    x, y = pygame.mouse.get_pos()
                    # print("posicion "+str(pygame.mouse.get_pos()))

                    # COMPARACIONES COINCIDENCIAS CLICK RATON CON POSICIONES DE LOS OBJETOS IMAGEN

                    if self.anular.collidepoint(x, y):

                        self.__init__()
                        self.opciones()

                    if self.confirmar.collidepoint(x, y):

                        if self.nombre == "":
                            self.mensaje = "No confio en alguien que no revela su nombre"
                            self.mi_mensaje = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 20)
                            # self.mi_nick_elegido.set_bold(True)
                            self.mi_mensaje = self.mi_mensaje.render(self.mensaje, 0, (255, 0, 0))
                            self.mi_mensaje = self.ventana_menu.blit(self.mi_mensaje, (475, 475))
                            #self.linea = pygame.draw.line(self.ventana_menu, (255, 0, 0), (475, 500), (975, 500),3)
                            self.sms = True

                        else:
                            conexion = sqlite3.connect('escapeRoom.db')
                            cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
                            lenguaje, encoding = getdefaultlocale()
                            #print(lenguaje[3:])
                            self.idioma = lenguaje[3:]
                            cursor.execute("INSERT INTO JUGADORES (nombre_jugador, nacionalidad) VALUES('" + self.nombre + "','" + self.idioma + "')")
                            conexion.commit()  # hacemos commit para lanzarlo
                            conexion.close()

                            return self.nombre
                            self.nick_elegido = True

            pygame.display.flip()

    def resetear(self):

        self.ventana_menu.blit(self.fondo_menu, (0, 0))
        self.rectangulo = pygame.draw.rect(self.ventana_menu, self.color_lineas_rectangulo, (450, 590, 600, 200), 1)

        if self.opcion_jugar_seleccionada:
            self.opcion_jugar = self.fuente.render("JUGAR", 0, (155, 155, 155))
            self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

            self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
            self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

            self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
            self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones, (635, 700))

            self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
            self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

            self.opcion_ranking_seleccionada = False
            self.opcion_instrucciones_seleccionada = False
            self.opcion_creditos_seleccionada = False

        if self.opcion_ranking_seleccionada:
            self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
            self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

            self.ranking = self.fuente.render("RANKING", 0, (155, 155, 155))
            self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

            self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
            self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,
                                                               (635, 700))

            self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
            self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

            self.opcion_jugar_seleccionada = False
            self.opcion_instrucciones_seleccionada = False
            self.opcion_creditos_seleccionada = False

        if self.opcion_instrucciones_seleccionada:
            self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
            self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

            self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
            self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

            self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (155, 155, 155))
            self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,
                                                               (635, 700))

            self.opcion_creditos = self.fuente.render("CREDITOS", 0, (255, 255, 255))
            self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

            self.opcion_jugar_seleccionada = False
            self.opcion_ranking_seleccionada = False
            self.opcion_creditos_seleccionada = False

        if self.opcion_creditos_seleccionada:
            self.opcion_jugar = self.fuente.render("JUGAR", 0, (255, 255, 255))
            self.opcion_jugar = self.ventana_menu.blit(self.opcion_jugar, (700, 600))

            self.ranking = self.fuente.render("RANKING", 0, (255, 255, 255))
            self.ranking = self.ventana_menu.blit(self.ranking, (685, 650))

            self.opcion_instrucciones = self.fuente.render("INSTRUCCIONES", 0, (255, 255, 255))
            self.opcion_instrucciones = self.ventana_menu.blit(self.opcion_instrucciones,
                                                               (635, 700))

            self.opcion_creditos = self.fuente.render("CREDITOS", 0, (155, 155, 155))
            self.opcion_creditos = self.ventana_menu.blit(self.opcion_creditos, (680, 750))

            self.opcion_jugar_seleccionada = False
            self.opcion_ranking_seleccionada = False
            self.opcion_instrucciones_seleccionada = False

    def listado_ranking(self):

        self.resetear()

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT nombre_jugador FROM JUGADORES WHERE id_jugador < 11")
        self.datos_jugadores = cursor.fetchall()  # guarda el primer registro y envia una tupla

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT nacionalidad FROM JUGADORES WHERE id_jugador < 11")
        self.nacion_jugadores = cursor.fetchall()  # guarda el primer registro y envia una tupla

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT tiempo_jugador FROM JUGADORES WHERE id_jugador < 11")
        self.superados = cursor.fetchall()  # guarda el primer registro y envia una tupla

        self.posicion_y = 40
        self.posicion_y2 = 35
        self.posicion_y3 = 40

        self.dic_jugadores = {}

        for self.datos_jugador in self.datos_jugadores:

            self.dic_jugadores = {'nombre': self.datos_jugador,'nacion': self.nacion_jugadores}

            self.mi_nick_elegido = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 22)
            #self.mi_nick_elegido.set_bold(True)
            self.mi_nick_elegido = self.mi_nick_elegido.render(self.dic_jugadores['nombre'][0], 0, (239, 127, 26))
            self.mi_nick_elegido = self.ventana_menu.blit(self.mi_nick_elegido, (500, self.posicion_y))

            self.posicion_y += 55

        for self.nacion_jugador in self.nacion_jugadores:
            self.dic_jugadores = {'nombre': self.datos_jugador, 'nacion': self.nacion_jugador}

            #print(self.dic_jugadores['nombre'][0], self.dic_jugadores['nacion'][0])
            #print(self.dic_jugadores['nacion'][0])
            df = pd.read_csv('./GeoLite2-Country-Locations-en.csv')
            self.pais_jugador = self.dic_jugadores['nacion'][0]
            #print(self.pais_jugador)
            self.pais_bandera = df[(df.country_iso_code == self.pais_jugador)].country_name.unique()
            self.pais_bandera = self.pais_bandera[0].lower()
            #print(self.pais_bandera)
            #print("./imagenes/png/"+self.pais_bandera+".png")
            self.bandera_mostrada= pygame.image.load("./imagenes/png/"+self.pais_bandera+".png")
            self.bandera_mostrada = pygame.transform.scale(self.bandera_mostrada, (40, 40))
            self.bandera_mostrada = self.ventana_menu.blit(self.bandera_mostrada, (730, self.posicion_y2))


            self.posicion_y2 += 55

        for self.superado in self.superados:
            self.dic_jugadores = {'nombre': self.datos_jugador, 'nacion': self.nacion_jugadores,'nivel': self.superado}

            self.mi_nivel = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 22)
            # self.mi_nivel.set_bold(True)
            self.mi_nivel = self.mi_nivel.render(self.dic_jugadores['nivel'][0], 0, (239, 127, 26))
            self.mi_nivel = self.ventana_menu.blit(self.mi_nivel, (925, self.posicion_y3))

            self.posicion_y3 += 55

        conexion.close()

    def instrucciones(self):

        self.resetear()
        # Recogemos el tiempo transcurrido cada vez que pase por este punto del juego

        self.tiempo_transcurrido = pygame.time.get_ticks()
        self.rango1 = self.tiempo_transcurrido - 1000
        self.rango2 = self.tiempo_transcurrido + 1000

        if self.rango1 < self.tiempo_transcurrido < self.rango2:

            if self.i == 0:
                self.mostrar_instruccion_1 = True
            if self.i == 15:
                self.mostrar_instruccion_1 = False
                self.mostrar_instruccion_2 = True
            if self.i == 40:
                self.mostrar_instruccion_2 = False
                self.mostrar_instruccion_3 = True
            if self.i == 65:
                self.mostrar_instruccion_3 = False
                self.mostrar_instruccion_4 = True
            if self.i == 90:
                self.mostrar_instruccion_4 = False
                self.mostrar_instruccion_5 = True
            if self.i == 115:
                self.mostrar_instruccion_5 = False
                self.mostrar_instruccion_6 = True
            if self.i == 140:
                self.mostrar_instruccion_6 = False
                self.opcion_instrucciones_seleccionada = False




            if self.mostrar_instruccion_1:
                # FONDO
                self.fondo_instrucciones = pygame.image.load("./imagenes/interior/fondo_instrucciones.png")
                self.fondo_instrucciones = pygame.transform.scale(self.fondo_instrucciones, (1100, 500))
                self.ventana_menu.blit(self.fondo_instrucciones, (200, 50))

                self.i += 1
                #print(self.i)

            if self.mostrar_instruccion_2:
                # FONDO
                self.fondo_instrucciones = pygame.image.load("./imagenes/interior/fondo_instrucciones.png")
                self.fondo_instrucciones = pygame.transform.scale(self.fondo_instrucciones, (1100, 500))
                self.ventana_menu.blit(self.fondo_instrucciones, (200, 50))

                self.flecha_instrucciones = pygame.image.load("./imagenes/flecha.png")
                self.flecha_instrucciones = pygame.transform.scale(self.flecha_instrucciones, (100, 60))
                self.ventana_menu.blit(self.flecha_instrucciones, (600, 50))

                self.texto_instruccion_1 = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.texto_instruccion_1 = self.texto_instruccion_1.render("Atento al tiempo", 0, (255, 255, 255))
                self.texto_instruccion_1 = self.ventana_menu.blit(self.texto_instruccion_1, (370, 65))

                self.i += 1
                #print(self.i)

            if self.mostrar_instruccion_3:
                # FONDO
                self.fondo_instrucciones = pygame.image.load("./imagenes/interior/fondo_instrucciones.png")
                self.fondo_instrucciones = pygame.transform.scale(self.fondo_instrucciones, (1100, 500))
                self.ventana_menu.blit(self.fondo_instrucciones, (200, 50))

                self.flecha_instrucciones_2 = pygame.image.load("./imagenes/flecha.png")
                self.flecha_instrucciones_2 = pygame.transform.scale(self.flecha_instrucciones_2, (100, 60))
                self.ventana_menu.blit(self.flecha_instrucciones_2, (1150, 220))

                self.texto_instruccion_2 = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.texto_instruccion_2 = self.texto_instruccion_2.render("Muevete por las salas", 0, (255, 255, 255))
                self.texto_instruccion_2 = self.ventana_menu.blit(self.texto_instruccion_2, (840, 235))

                self.i += 1
                #print(self.i)

            if self.mostrar_instruccion_4:
                # FONDO
                self.fondo_instrucciones = pygame.image.load("./imagenes/interior/fondo_instrucciones.png")
                self.fondo_instrucciones = pygame.transform.scale(self.fondo_instrucciones, (1100, 500))
                self.ventana_menu.blit(self.fondo_instrucciones, (200, 50))

                self.flecha_instrucciones_3 = pygame.image.load("./imagenes/flecha.png")
                self.flecha_instrucciones_3 = pygame.transform.scale(self.flecha_instrucciones_3, (100, 60))
                self.flecha_instrucciones_3 = pygame.transform.rotate(self.flecha_instrucciones_3, 180)
                self.ventana_menu.blit(self.flecha_instrucciones_3, (320, 400))

                self.texto_instruccion_3 = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.texto_instruccion_3 = self.texto_instruccion_3.render("Encuentra objetos", 0, (255, 255, 255))
                self.texto_instruccion_3 = self.ventana_menu.blit(self.texto_instruccion_3, (410, 415))

                self.i += 1
                #print(self.i)

            if self.mostrar_instruccion_5:
                # FONDO
                self.fondo_instrucciones = pygame.image.load("./imagenes/interior/fondo_instrucciones.png")
                self.fondo_instrucciones = pygame.transform.scale(self.fondo_instrucciones, (1100, 500))
                self.ventana_menu.blit(self.fondo_instrucciones, (200, 50))

                self.flecha_instrucciones_4 = pygame.image.load("./imagenes/flecha.png")
                self.flecha_instrucciones_4 = pygame.transform.scale(self.flecha_instrucciones_4, (100, 60))
                self.flecha_instrucciones_4 = pygame.transform.rotate(self.flecha_instrucciones_4, 90)
                self.ventana_menu.blit(self.flecha_instrucciones_4, (1120, 400))

                self.texto_instruccion_4 = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.texto_instruccion_4 = self.texto_instruccion_4.render("Mira las ayudas", 0, (255, 255, 255))
                self.texto_instruccion_4 = self.ventana_menu.blit(self.texto_instruccion_4, (1010, 380))

                self.i += 1
                #print(self.i)

            if self.mostrar_instruccion_6:
                # FONDO
                self.fondo_instrucciones = pygame.image.load("./imagenes/interior/fondo_instrucciones_3.png")
                self.fondo_instrucciones = pygame.transform.scale(self.fondo_instrucciones, (1100, 500))
                self.ventana_menu.blit(self.fondo_instrucciones, (200, 50))

                self.flecha_instrucciones_5 = pygame.image.load("./imagenes/flecha.png")
                self.flecha_instrucciones_5 = pygame.transform.scale(self.flecha_instrucciones_5, (100, 60))
                self.flecha_instrucciones_5 = pygame.transform.rotate(self.flecha_instrucciones_5, 230)
                self.ventana_menu.blit(self.flecha_instrucciones_5, (250, 400))

                self.texto_instruccion_5 = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.texto_instruccion_5 = self.texto_instruccion_5.render("Selecciona objetos para crear y usar", 0, (255, 255, 255))
                self.texto_instruccion_5 = self.ventana_menu.blit(self.texto_instruccion_5, (340, 415))

                self.i += 1
                #print(self.i)

            # Aumentamos 1 segundo el contador del reloj

            self.rango1 += 1000
            self.rango2 += 1000


    def creditos(self):

        #print("rango 1 " + str(self.rango1))
        #print("tiempo " + str(self.tiempo_transcurrido))
        #print("rango 2 " + str(self.rango2))
        #print("")
        #print("posicion 1 " + str(self.y))
        #print("")

        # Recogemos el tiempo transcurrido cada vez que pase por este punto del juego

        self.tiempo_transcurrido = pygame.time.get_ticks()
        self.rango1 = self.tiempo_transcurrido - 1000
        self.rango2 = self.tiempo_transcurrido + 1000

        if self.rango1 < self.tiempo_transcurrido < self.rango2:

            self.resetear()

            if self.y == 0:
                self.mostrar_designer = True
            if self.y == 200:
                self.mostrar_creado = True
            if self.y == 450:
                self.mostrar_designer = False
            if self.y2 == 200:
                self.mostrar_copyrght = True
            if self.y2 == 450:
                self.mostrar_creado = False
            if self.y3 == 450:
                self.mostrar_copyrght = False
                self.opcion_creditos_seleccionada = False
                self.y = 0
                self.y2 = 0
                self. y3 = 0



            if self.mostrar_designer:

                self.designer = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 25)
                self.designer.set_bold(True)
                self.designer = self.designer.render("AUTOR", 0, (155, 155, 155))
                self.designer = self.ventana_menu.blit(self.designer, (575, (self.y + 50)))

                self.imagen_designer = pygame.image.load("./imagenes/designer.png")
                self.imagen_designer = pygame.transform.scale(self.imagen_designer, (125, 125))
                self.imagen_designer = self.ventana_menu.blit(self.imagen_designer, (775, self.y))

                self.jmaga = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.jmaga = self.jmaga.render("@JMaga", 0, (255, 255, 255))
                self.jmaga = self.ventana_menu.blit(self.jmaga, (850, (self.y + 50)))

                self.y += 2

            if self.mostrar_creado:

                self.creado = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 25)
                self.creado.set_bold(True)
                self.creado = self.creado.render("CREADO CON", 0, (155, 155, 155))
                self.creado = self.ventana_menu.blit(self.creado, (560, (self.y2 + 50)))

                self.imagen_creado = pygame.image.load("./imagenes/pygame.png")
                self.imagen_creado = pygame.transform.scale(self.imagen_creado, (200, 125))
                self.imagen_creado = self.ventana_menu.blit(self.imagen_creado, (775, self.y2))

                self.y2 += 2

            if self.mostrar_copyrght:
                self.designer = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 25)
                self.designer.set_bold(True)
                self.designer = self.designer.render("COPYRIGHT", 0, (155, 155, 155))
                self.designer = self.ventana_menu.blit(self.designer, (575, (self.y3 + 50)))

                self.imagen_designer = pygame.image.load("./imagenes/copyright.png")
                self.imagen_designer = pygame.transform.scale(self.imagen_designer, (125, 125))
                self.imagen_designer = self.ventana_menu.blit(self.imagen_designer, (775, self.y3))

                self.jmaga = pygame.font.Font("./fuentes/JetBrainsMono-Italic.ttf", 25)
                # self.designer .set_bold(True)
                self.jmaga = self.jmaga.render("2020 @JMaga", 0, (255, 255, 255))
                self.jmaga = self.ventana_menu.blit(self.jmaga, (865, (self.y3 + 50)))

                self.y3+= 2


            # Aumentamos 1 segundo el contador del reloj

            self.rango1 += 1000
            self.rango2 += 1000






