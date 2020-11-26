# MODULOS
import sqlite3

import pygame
import sys

class EscapeRoom:

    def __init__(self):

        conexion = sqlite3.connect('escapeRoom.db')
        cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
        cursor.execute("SELECT nombre_jugador FROM JUGADORES order by id_jugador DESC limit 1")
        self.nombre = cursor.fetchone()
        #print(self.nombre[0])
        conexion.commit()  # hacemos commit para lanzarlo
        conexion.close()

        """ INICIO DE MUSICA DE FONDO
        ------------------------------- """

        pygame.mixer_music.load("./musica/musica_fondo.mp3")
        pygame.mixer_music.play(-1)

        """ CREACION DE PANTALLA INICIAL
        ----------------------------------- """

        self.ventana_juego = pygame.display.set_mode((1920, 1050))
        pygame.display.set_caption("Scape Room")

        """ IMAGENES DE INICIO
        ------------------------- """

        # FONDO
        self.fondo1 = pygame.image.load("./imagenes/interior.jpg")
        self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
        self.ventana_juego.blit(self.fondo1, (0, 0))

        # INVENTARIO

        self.color_rectangulo = (0, 0, 0)
        self.color_cuadrado_construido = (40, 210, 250)
        self.color_cuadrado = (120, 120, 120)
        self.color_cuadrado_seleccionado = (0, 210, 0)

        self.rectangulo = pygame.draw.rect(self.ventana_juego, self.color_rectangulo, (0, 880, 1920, 130), 0)
        self.casilla1 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (3, 890, 130, 110), 5)
        self.casilla2 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (228, 890, 130, 110), 5)
        self.casilla3 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (453, 890, 130, 110), 5)
        self.casilla4 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (678, 890, 130, 110), 5)
        self.casilla5 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (903, 890, 130, 110), 5)
        self.casilla6 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_construido, (1128, 890, 130, 110), 5)

        # BOTONES CREAR / USAR
        self.boton_usar = pygame.image.load("./imagenes/boton_usar.png")
        self.boton_usar = pygame.transform.scale(self.boton_usar, (100, 75))
        self.boton_usar = self.ventana_juego.blit(self.boton_usar, (1300, 885))

        self.boton_usar_texto = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
        self.boton_usar_texto.set_bold(True)
        self.boton_usar_texto = self.boton_usar_texto.render('USAR', 0, (90, 90, 90))
        self.boton_usar_texto = self.ventana_juego.blit(self.boton_usar_texto, (1330, 915))

        self.boton_crear = pygame.image.load("./imagenes/boton_combinar.png")
        self.boton_crear = pygame.transform.scale(self.boton_crear, (100, 75))
        self.boton_crear = self.ventana_juego.blit(self.boton_crear, (1300, 935))

        self.boton_crear_texto = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
        self.boton_crear_texto.set_bold(True)
        self.boton_crear_texto = self.boton_crear_texto.render('CREAR', 0, (90, 90, 90))
        self.boton_crear_texto = self.ventana_juego.blit(self.boton_crear_texto, (1325, 965))

        # CONTROL CYBORG

        self.cyborg = pygame.image.load("./imagenes/cyborg.jpg")
        self.cyborg = pygame.transform.scale(self.cyborg, (400, 150))
        self.cyborg = self.ventana_juego.blit(self.cyborg, (1450, 880))

        self.cyborg_texto= pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 15)
        self.cyborg_texto = self.cyborg_texto.render('CONTROL EXTERNO ACTIVADO', 0, (0, 255, 0))
        self.cyborg_texto = self.ventana_juego.blit(self.cyborg_texto, (1550, 1030))


        # BOTON VOLUMEN

        self.volumen = pygame.image.load("./imagenes/volumen_on.png")
        self.volumen = pygame.transform.scale(self.volumen, (30, 30))
        self.volumen = self.ventana_juego.blit(self.volumen, (1875, 900))


        # TEMPORIZADOR

        self.fuente = pygame.font.Font(None, 100)

        # OBJETOS

        self.voltaje = pygame.image.load("./imagenes/interior/anclaje_energia.png")
        self.voltaje = pygame.transform.scale(self.voltaje, (250, 160))
        self.voltaje = pygame.transform.rotate(self.voltaje, 200)
        self.voltaje = self.ventana_juego.blit(self.voltaje, (450, 560))

        self.taza = pygame.image.load("./imagenes/interior/taza_termica_huella.png")
        self.taza = pygame.transform.scale(self.taza, (70, 110))
        # self.taza = pygame.transform.rotate(self.taza, 200)
        self.taza = self.ventana_juego.blit(self.taza, (1040, 690))

        self.cinta = pygame.image.load("./imagenes/interior/cinta_adhesiva.png")
        self.cinta = pygame.transform.scale(self.cinta, (10, 15))
        # self.taza = pygame.transform.rotate(self.taza, 200)
        self.cinta = self.ventana_juego.blit(self.cinta, (1040, 690))

        """ VARIABLES DE CONTROL
        ---------------------------"""

        # ESTADOS COMPROBACIONES

        # salas

        self.sala1 = True
        self.sala_intermedia_derecha = False
        self.sala1_derecha = False
        self.sala1_derecha_escaleras = False
        self.sala1_derecha_hacker = False
        self.sala_intermedia_izquierda = False
        self.sala1_izquierda = False

        self.escenario = None
        self.salir = False

        # objetos

        self.palanca = False

        self.mirar_persiana = False
        self.persina_abierta = False
        self.trampilla_descubierta = False
        self.mirar_trampilla = False

        self.mirar_escalera_arriba = False
        self.cableado_activo = False

        self.taza_encontrado = False

        self.cinta_encontrado = False

        self.caja_voltaje = True
        self.caja_voltaje_aumentada = False
        self.voltaje_encontrado = False
        self.voltaje_usado = False
        self.bajar_escalera = False
        self.rejilla_abierta = False

        self.mirar_caja_electrica = False
        self.electricidad_reestablecida = False
        self.mirar_lector_huellas = False
        self.lector_huellas_activado = False
        self.huella_usada = False

        self.puerta_abierta = False

        self.mostrar_superobjeto = False
        self.superobjeto_encontrado = False

        self.encuentro1 = False
        self.casilla1_ocupada = False
        self.casilla1_seleccionada = False

        self.casilla2_ocupada = False
        self.casilla2_seleccionada = False

        self.casilla3_ocupada = False
        self.casilla3_seleccionada = False

        self.casilla4_ocupada = False
        self.casilla4_seleccionada = False

        self.casilla5_ocupada = False
        self.casilla5_seleccionada = False

        self.casilla6_ocupada = False
        self.casilla6_seleccionada = False

        self.musica_parada = False

        # TIEMPO

        self.tiempo_transcurrido = pygame.time.get_ticks()

        self.rango1 = self.tiempo_transcurrido - 1000
        self.rango2 = self.tiempo_transcurrido + 1000

        self.segundero = 0
        self.minutero = 60
        self.cont = 0

        self.juego_superado = False
        self.tiempo_terminado = False

        self.tiempo_mostrar_imagen = 0
        self.tiempo_mostrar_info_palanca = -1
        self.tiempo_mostrar_info_voltaje = -1
        self.tiempo_mostrar_info_puerta = -1
        self.tiempo_mostrar_info_persiana = -1
        self.tiempo_mostrar_info_trampilla = -1
        self.tiempo_mostrar_info_escalera_arriba = -1
        self.tiempo_mostrar_info_caja_electrica = -1
        self.tiempo_mostrar_info_lector_huellas = -1
        self.tiempo_mostrar_info_taza = -1
        self.tiempo_mostrar_info_cinta = -1
        self.tiempo_mostrar_info_superobjeto = -1

    def juego(self):

        """ PUESTA EN MARCHA DEL JUEGO
        ---------------------------------"""

        # BUCLE HASTA FINALIZACION

        while not self.salir:

            """GESTION DEL TIEMPO
            ------------------------"""

            # Recogemos el tiempo transcurrido cada vez que pase por este punto del juego

            self.tiempo_transcurrido = pygame.time.get_ticks()

            # LLAMADA A LA FUNCION RELOJ

            self.reloj()

            """ ENTRADAS DE TECLADO Y RATON 
            ---------------------------------"""

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
                    #print("posicion "+str(pygame.mouse.get_pos()))

                    # COMPARACIONES COINCIDENCIAS CLICK RATON CON POSICIONES DE LOS OBJETOS IMAGEN

                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA 1
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.objeto1.collidepoint(x, y) and not self.encuentro1 and self.sala1:

                        # reanuadamos tiempo que se mostrara el objeto encontrado en tamano grande en pantalla

                        self.tiempo_mostrar_imagen = 0

                        # imagen estrella que marca que se ha encontrado un objeto

                        self.estrella = pygame.image.load("./imagenes/estrella.png")
                        self.estrella = pygame.transform.scale(self.estrella, (120, 80))
                        self.estrella = pygame.transform.rotate(self.estrella, 110)
                        self.ventana_juego.blit(self.estrella, (170, 725))

                        # cambiamos estado comprobacion a objeto encontrado

                        self.encuentro1 = True

                    if self.rect_palanca.collidepoint(x, y) and not self.palanca and self.sala1:

                        self.tiempo_mostrar_info_palanca = 0

                    if self.flecha_derecha.collidepoint(x, y) and self.sala1:

                        self.sala1 = False
                        self.sala_intermedia_derecha = True

                        break

                    if self.flecha_izquierda.collidepoint(x, y) and self.sala1:

                        self.sala1 = False
                        self.sala_intermedia_izquierda = True

                        break

                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA INTERMEDIA DERECHA
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.flecha_derecha.collidepoint(x, y) and self.sala_intermedia_derecha:

                        self.sala1_derecha = True
                        self.sala_intermedia_derecha = False

                        break

                    if self.flecha_izquierda.collidepoint(x, y) and self.sala_intermedia_derecha:

                        self.sala1 = True
                        self.sala_intermedia_derecha = False

                        break

                    if self.rect_persiana.collidepoint(x, y) and self.sala_intermedia_derecha and not self.persina_abierta:

                        self.mirar_persiana = True
                        self.tiempo_mostrar_info_persiana = 0

                    if self.rect_trampilla.collidepoint(x, y) and self.sala_intermedia_derecha and not self.trampilla_descubierta:
                        self.mirar_trampilla = True
                        self.tiempo_mostrar_info_trampilla = 0

                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA DERECHA
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.rect_caja_voltaje.collidepoint(x, y) and self.caja_voltaje and self.sala1_derecha:

                        self.sala1_derecha = False
                        self. caja_voltaje = False
                        self.caja_voltaje_aumentada = True

                    if self.voltaje.collidepoint(x, y) and self.caja_voltaje_aumentada and not self.voltaje_encontrado:

                        self.tiempo_mostrar_info_voltaje = 0

                        # reanuadamos tiempo que se mostrara el objeto encontrado en tamano grande en pantalla

                        self.tiempo_mostrar_imagen = 0

                        # imagen estrella que marca que se ha encontrado un objeto

                        self.estrella = pygame.image.load("./imagenes/estrella.png")
                        self.estrella = pygame.transform.scale(self.estrella, (120, 80))
                        self.estrella = pygame.transform.rotate(self.estrella, 110)
                        self.ventana_juego.blit(self.estrella, (500, 620))

                        # cambiamos estado comprobacion a objeto encontrado

                        self.voltaje_encontrado = True

                    if self.rect_rejilla.collidepoint(x, y) and not self.rejilla_abierta and self.sala1_derecha:
                        self.bajar_escalera = True
                        self.tiempo_mostrar_info_rejilla = 0

                    if self.rect_rejilla.collidepoint(x ,y) and self.rejilla_abierta and self.sala1_derecha:
                        self.sala1_derecha_escaleras = True
                        self.sala1_derecha = False

                    if self.flecha_izquierda.collidepoint(x, y) and self.sala1_derecha:

                        self.sala_intermedia_derecha = True
                        self.sala1_derecha = False

                        break

                    if self.rect_escalera_arriba.collidepoint(x, y) and self.sala1_derecha and not self.cableado_activo:
                        self.mirar_escalera_arriba = True
                        self.tiempo_mostrar_info_escalera_arriba = 0

                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA DERECHA ESCALERAS
                    # ----------------------------------------------------------------------------------------------------------------
                    if self.flecha_derecha.collidepoint(x, y) and self.sala1_derecha_escaleras:

                        self.sala1_derecha_hacker = True
                        self.sala1_derecha_escaleras = False

                        break

                    if self.flecha_izquierda.collidepoint(x, y) and self.sala1_derecha_escaleras:

                        self.sala1_derecha = True
                        self.sala1_derecha_escaleras = False

                        break

                    if self.cinta.collidepoint(x, y) and self.sala1_derecha_escaleras:
                        self.tiempo_mostrar_info_cinta = 0

                        # reanuadamos tiempo que se mostrara el objeto encontrado en tamano grande en pantalla

                        self.tiempo_mostrar_imagen = 0

                        # imagen estrella que marca que se ha encontrado un objeto

                        self.estrella = pygame.image.load("./imagenes/estrella.png")
                        self.estrella = pygame.transform.scale(self.estrella, (120, 80))
                        self.estrella = pygame.transform.rotate(self.estrella, 110)
                        self.ventana_juego.blit(self.estrella, (1000, 620))

                        # cambiamos estado comprobacion a objeto encontrado

                        self.cinta_encontrado = True
                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA DERECHA HACKER
                    # ----------------------------------------------------------------------------------------------------------------
                    if self.flecha_izquierda.collidepoint(x, y) and self.sala1_derecha_hacker:

                        self.sala1_derecha_escaleras = True
                        self.sala1_derecha_hacker = False

                        break

                    if self.taza.collidepoint(x, y) and self.sala1_derecha_hacker:
                        self.tiempo_mostrar_info_taza = 0

                        # reanuadamos tiempo que se mostrara el objeto encontrado en tamano grande en pantalla

                        self.tiempo_mostrar_imagen = 0

                        # imagen estrella que marca que se ha encontrado un objeto

                        self.estrella = pygame.image.load("./imagenes/estrella.png")
                        self.estrella = pygame.transform.scale(self.estrella, (120, 80))
                        self.estrella = pygame.transform.rotate(self.estrella, 110)
                        self.ventana_juego.blit(self.estrella, (1000, 620))

                        # cambiamos estado comprobacion a objeto encontrado

                        self.taza_encontrado = True

                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA INTERMEDIA IZQUIERDA
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.flecha_derecha.collidepoint(x, y) and self.sala_intermedia_izquierda:

                        self.sala1 = True
                        self.sala_intermedia_izquierda = False

                        break

                    if self.flecha_izquierda.collidepoint(x, y) and self.sala_intermedia_izquierda:

                        self.sala1_izquierda = True
                        self.sala_intermedia_izquierda = False

                        break



                    if self.rect_caja_electrica.collidepoint(x, y) and self.sala_intermedia_izquierda and not self.electricidad_reestablecida:
                        self.mirar_caja_electrica = True
                        self.sala_intermedia_izquierda = False
                        self.tiempo_mostrar_info_caja_electrica = 0

                        break

                    if self.rect_caja_lector_huellas.collidepoint(x, y) and self.sala_intermedia_izquierda and not self.lector_huellas_activado:
                        self.mirar_lector_huellas = True
                        self.sala_intermedia_izquierda = False
                        self.tiempo_mostrar_info_lector_huellas = 0

                        break

                    if self.flecha_derecha.collidepoint(x, y) and self.mirar_lector_huellas:
                        self.mirar_lector_huellas = False
                        self.sala_intermedia_izquierda = True

                        if not self.musica_parada:
                            pygame.mixer_music.load("./musica/musica_fondo.mp3")
                            pygame.mixer_music.play(-1)
                        break

                    if self.flecha_izquierda.collidepoint(x, y) and self.mirar_caja_electrica:
                        self.mirar_caja_electrica = False
                        self.sala_intermedia_izquierda = True

                        if not self.musica_parada:
                            pygame.mixer_music.load("./musica/musica_fondo.mp3")
                            pygame.mixer_music.play(-1)

                        break
                    # ----------------------------------------------------------------------------------------------------------------
                    # SALA IZQUIERDA
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.flecha_derecha.collidepoint(x, y) and self.sala1_izquierda:

                        self.sala1_izquierda = False
                        self.sala_intermedia_izquierda = True

                        if not self.musica_parada:
                            pygame.mixer_music.load("./musica/musica_fondo.mp3")
                            pygame.mixer_music.play(-1)

                        break

                    if self.rect_puerta.collidepoint(x, y) and self.sala1_izquierda:

                        pygame.mixer_music.load("./musica/cierre.mp3")
                        pygame.mixer_music.play()

                        self.tiempo_mostrar_info_puerta = 0

                    # GESTION DEL VOLUMEN

                    elif self.volumen.collidepoint(x, y) and not self.musica_parada:

                        # imagen de icono volumen apagado

                        self.volumen = pygame.image.load("./imagenes/volumen_off.png")
                        self.volumen = pygame.transform.scale(self.volumen, (30, 30))
                        self.volumen = self.ventana_juego.blit(self.volumen, (1875, 900))

                        # pausamos musica

                        pygame.mixer_music.pause()

                        # cambiamos estado musica a pausada

                        self.musica_parada = True

                    elif self.volumen.collidepoint(x, y) and self.musica_parada:

                        # imagen icono volumen encendido

                        self.volumen = pygame.image.load("./imagenes/volumen_on.png")
                        self.volumen = pygame.transform.scale(self.volumen, (30, 30))
                        self.volumen = self.ventana_juego.blit(self.volumen, (1875, 900))

                        # reaudamos musica

                        pygame.mixer_music.load("./musica/musica_fondo.mp3")
                        pygame.mixer_music.play(-1)

                        # cambiamos estado musica a sonando

                        self.musica_parada = False

                    # GESTION CASILLAS SELECCIONADAS

                    elif self.casilla1.collidepoint(x, y) and self.casilla1_ocupada and not self.casilla1_seleccionada:

                        # Remarcamos casilla seleccionada

                        self.casilla1 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_seleccionado,
                                                         (3, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a seleccionada

                        self.casilla1_seleccionada = True


                    elif self.casilla1.collidepoint(x, y) and self.casilla1_ocupada and self.casilla1_seleccionada:

                        # quitamos marcacion a la casilla como no seleccionada

                        self.casilla1 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (3, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a no sellecioneda

                        self.casilla1_seleccionada = False



                    elif self.casilla2.collidepoint(x, y) and self.casilla2_ocupada and not self.casilla2_seleccionada:

                        # Remarcamos casilla seleccionada

                        self.casilla2 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_seleccionado,
                                                         (228, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a seleccionada

                        self.casilla2_seleccionada = True



                    elif self.casilla2.collidepoint(x, y) and self.casilla2_ocupada and self.casilla2_seleccionada:

                        # quitamos marcacion a la casilla como no seleccionada

                        self.casilla2 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado,  (228, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a no sellecioneda

                        self.casilla2_seleccionada = False



                    elif self.casilla3.collidepoint(x, y) and self.casilla3_ocupada and not self.casilla3_seleccionada:

                        # Remarcamos casilla seleccionada

                        self.casilla3 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_seleccionado,
                                                         (453, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a seleccionada

                        self.casilla3_seleccionada = True



                    elif self.casilla3.collidepoint(x, y) and self.casilla3_ocupada and self.casilla3_seleccionada:

                        # quitamos marcacion a la casilla como no seleccionada

                        self.casilla3 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (453, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a no sellecioneda

                        self.casilla3_seleccionada = False

                    elif self.casilla4.collidepoint(x, y) and self.casilla4_ocupada and not self.casilla4_seleccionada:

                        # Remarcamos casilla seleccionada

                        self.casilla4 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_seleccionado,
                                                         (678, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a seleccionada

                        self.casilla4_seleccionada = True



                    elif self.casilla4.collidepoint(x, y) and self.casilla4_ocupada and self.casilla4_seleccionada:

                        # quitamos marcacion a la casilla como no seleccionada

                        self.casilla4 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado, (678, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a no sellecioneda

                        self.casilla4_seleccionada = False

                    elif self.casilla6.collidepoint(x, y) and self.casilla6_ocupada and not self.casilla6_seleccionada:

                        # Remarcamos casilla seleccionada

                        self.casilla6 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_seleccionado,
                                                         (1128, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a seleccionada

                        self.casilla6_seleccionada = True



                    elif self.casilla6.collidepoint(x, y) and self.casilla6_ocupada and self.casilla6_seleccionada:

                        # quitamos marcacion a la casilla como no seleccionada

                        self.casilla6 = pygame.draw.rect(self.ventana_juego, self.color_cuadrado_construido, (1128, 890, 130, 110), 5)

                        # cambiamos el estado de la casilla a no sellecioneda

                        self.casilla6_seleccionada = False

                    # ----------------------------------------------------------------------------------------------------------------
                    # CREAR SUPEROBJETOS
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.boton_crear.collidepoint(x, y) and self.casilla3_seleccionada and self.casilla4_seleccionada and self.mirar_lector_huellas and not self.casilla1_seleccionada:

                        self.tiempo_mostrar_info_superobjeto = 0

                        self.tiempo_mostrar_imagen = 0

                        self.superobjeto_encontrado = True
                        self.mostrar_superobjeto = True

                    # ----------------------------------------------------------------------------------------------------------------
                    # USO OBJETOS
                    # ----------------------------------------------------------------------------------------------------------------

                    if self.boton_usar.collidepoint(x, y) and self.mirar_caja_electrica and self.casilla2_seleccionada:
                        self.voltaje_usado = True

                        self.casilla2_ocupada = False

                    if self.boton_usar.collidepoint(x, y) and self.mirar_lector_huellas and self.casilla6_seleccionada  and self.voltaje_usado:
                        self.huella_usada = True

                        self.casilla6_ocupada = False

                    if self.rect_puerta.collidepoint(x, y) and self.sala1_izquierda and self.casilla1_seleccionada and self.voltaje_usado and self.huella_usada:
                        self.puerta_abierta = True
                        self.cont = 0
                        self.casilla1_ocupada = False

            # detectamos acciones
            # self.escenario.click_accion()

            # actualizamos el escenario
            # self.escenario.click_actualizar()

            # dibujamos la pantalla con su nuevo escenario
            # self.escenario.pintar(self.ventana_juego)

            """ ACTUALIZAMOS PANTALLA 
            -----------------------------"""

            # Actualizamos la pantallla completa, en caso de querer actualizar una parte lo pasaremos por funcion en pygame.display.update()

            pygame.display.flip()

    """ FUNCION DE GESTION DE TIEMPO Y CONTROL DE ACCIONES 
    ---------------------------------------------------------"""

    def reloj(self):

        if self.rango1 < self.tiempo_transcurrido < self.rango2:

            if self.segundero < 10:

                # Mostramos ventana para no sobre escribir los numeros y se renueve la imagen

                self.ventana_juego.blit(self.fondo1, (0, 0))

                # LLAMADA A LA FUNCION DE ACTUALIZACION DE LOS SUCESOS DE IMAGENES CADA SEGUNDO

                self.actualizar()

                # Mostramos reloj nuevo en pantalla

                self.mensaje = self.fuente.render(str(self.minutero) + ":" + '0' + str(self.segundero), 0, (255, 0, 0))
                self.ventana_juego.blit(self.mensaje, (875, 30))

            else:

                # Mostramos ventana para no sobre escribir los numeros y se renueve la imagen

                self.ventana_juego.blit(self.fondo1, (0, 0))

                # LLAMADA A LA FUNCION DE ACTUALIZACION DE LOS SUCESOS DE IMAGENES CADA SEGUNDO

                self.actualizar()

                # Mostramos reloj nuevo en pantalla

                self.mensaje = self.fuente.render(str(self.minutero) + ":" + str(self.segundero), 0, (255, 0, 0))
                self.ventana_juego.blit(self.mensaje, (875, 30))

            # Aumentamos 1 segundo el contador del reloj

            self.rango1 += 1000
            self.rango2 += 1000

            # Gestion del segundero

            self.segundero -= 1

            # print(self.tiempo_transcurrido)
            # print(self.rango1)
            # print(self.rango2)

            # TIEMPO DE 10 MIN PARA LA DEMO

            if self.minutero >= 49 and self.puerta_abierta:
                self.fuente_info = pygame.font.Font("./fuentes/ABCThru.ttf", 150)
                self.superado = self.fuente_info.render("SUCCESS", 0, (0, 255, 0))
                self.superado = self.ventana_juego.blit(self.superado, (660, 350))

                self.juego_superado = True
                self.tiempo_terminado = True

                conexion = sqlite3.connect('escapeRoom.db')
                cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
                cursor.execute("UPDATE JUGADORES SET tiempo_jugador='SUCCESS' WHERE nombre_jugador='" + self.nombre[0] + "'")
                cursor.execute("delete from JUGADORES where id_jugador not in (select max(id_jugador) from JUGADORES group by nombre_jugador)")
                conexion.commit()  # hacemos commit para lanzarlo
                conexion.close()

                self.cont += 1

                if self.cont == 10:
                    pygame.quit()

            if self.minutero == 49 and not self.puerta_abierta:
                self.fuente_info = pygame.font.Font("./fuentes/ABCThru.ttf", 150)
                self.no_superado = self.fuente_info.render("FAIL", 0, (255, 0, 0))
                self.no_superado = self.ventana_juego.blit(self.no_superado, (800, 320))

                self.juego_superado = False
                self.tiempo_terminado = True

                conexion = sqlite3.connect('escapeRoom.db')
                cursor = conexion.cursor()  # generamos un objeto de conexion, (crud,ddl,dml...)
                cursor.execute("UPDATE JUGADORES SET tiempo_jugador='FAIL' WHERE nombre_jugador='"+self.nombre[0]+"'")
                cursor.execute("delete from JUGADORES where id_jugador not in (select max(id_jugador) from JUGADORES group by nombre_jugador)")
                conexion.commit()  # hacemos commit para lanzarlo
                conexion.close()

                if self.segundero == 55:
                    pygame.quit()

            # Salida cuando el tiempo del temporizador llegue a 0

            if self.segundero == 0 and self.minutero == 0:
                sys.exit()

            # Gestion del reloj

            elif self.segundero < 0 and self.minutero != 0:
                self.segundero = 59
                self.minutero -= 1
            return self.rango1, self.rango2

    """ FUNCION ACTUALIZAR IMAGENES UTILIZADAS
    ---------------------------------------------"""

    def actualizar(self):

        # ----------------------------------------------------------------------------------------------------------------
        # SALA 1
        # ----------------------------------------------------------------------------------------------------------------

        if self.sala1:
            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            self.resetear_flecha_derecha()
            self.resetear_cyborg()

            # GESTION DE OBJETO ENCONTRADO

            if not self.palanca:


                if 0 <= self.tiempo_mostrar_info_palanca <= 3:
                    self.cyborg_texto_info_palanca = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_palanca = self.cyborg_texto_info_palanca.render('La palanca esta atorada', 0,
                                                                                           (255, 255, 255))
                    self.cyborg_texto_info_palanca = self.ventana_juego.blit(self.cyborg_texto_info_palanca,
                                                                             (1565, 950))

                    self.tiempo_mostrar_info_palanca += 1

                    if self.tiempo_mostrar_info_palanca == 1:
                        pygame.mixer_music.load("./musica/palanca.mp3")
                        pygame.mixer_music.play()
                    if self.tiempo_mostrar_info_palanca == 3 and not self.musica_parada:
                        pygame.mixer_music.load("./musica/musica_fondo.mp3")
                        pygame.mixer_music.play(-1)

                else:
                    self.resetear_cyborg()


                if not self.encuentro1:

                    # posicion inicial del objeto antes de ser encontrado

                    self.objeto1 = pygame.image.load("./imagenes/medallon.png")
                    self.objeto1 = pygame.transform.scale(self.objeto1, (30, 15))
                    self.objeto1 = self.ventana_juego.blit(self.objeto1, (210, 788))

                else:

                    # TIEMPO QUE SE MUESTRA LA IMAGEN EN GRANDE Y CENTRADA

                    # cuando transcurran 2 segundos quitaremos la imagen del centro

                    if self.tiempo_mostrar_imagen == 2:

                        # mostramos el fondo inicial

                        # self.ventana_juego.blit(self.fondo1, (0, 0))

                        # Cambiamos el estado de la casilla que ocupara la imagen del objeto encontrado

                        self.casilla1_ocupada = True

                    else:

                        # Mostramos la imagen del objeto encontardo en el centro durante 2 segundos

                        self.objeto1_encontrado = pygame.image.load("./imagenes/medallon.png")
                        self.objeto1_encontrado = pygame.transform.scale(self.objeto1_encontrado, (500, 500))
                        self.ventana_juego.blit(self.objeto1_encontrado, (700, 185))

                        self.tiempo_mostrar_imagen += 1

        # ----------------------------------------------------------------------------------------------------------------
        # SALA INTERMEDIA DERECHA
        # ----------------------------------------------------------------------------------------------------------------

        if self.sala_intermedia_derecha:
            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_intermedia_dcha.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if self.mirar_persiana and not self.persina_abierta:
                # FONDO
                self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_intermedia_dcha_persiana.jpg")
                self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
                self.ventana_juego.blit(self.fondo1, (0, 0))

                if 0 <= self.tiempo_mostrar_info_persiana <= 3:
                    self.cyborg_texto_info_bajar = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_bajar = self.cyborg_texto_info_bajar.render('Debo abrir la persiana', 0,
                                                                                       (255, 255, 255))
                    self.cyborg_texto_info_bajar = self.ventana_juego.blit(self.cyborg_texto_info_bajar,
                                                                           (1580, 950))

                    self.tiempo_mostrar_info_persiana += 1

                else:
                    self.resetear_cyborg()

                    self.mirar_persiana = False

            if not self.trampilla_descubierta and self.mirar_trampilla:
                # FONDO
                self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_intermedia_dcha_trampilla.jpg")
                self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
                self.ventana_juego.blit(self.fondo1, (0, 0))

                if self.tiempo_mostrar_info_trampilla == 0:
                    pygame.mixer_music.load("./musica/palanca.mp3")
                    pygame.mixer_music.play()
                if self.tiempo_mostrar_info_trampilla == 1:
                    pygame.mixer_music.load("./musica/reja.mp3")
                    pygame.mixer_music.play()

                if self.tiempo_mostrar_info_trampilla == 3 and not self.musica_parada:
                    pygame.mixer_music.load("./musica/musica_fondo.mp3")
                    pygame.mixer_music.play(-1)

                if 0 <= self.tiempo_mostrar_info_trampilla <= 3:
                    self.cyborg_texto_info_trampilla = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_trampilla = self.cyborg_texto_info_trampilla.render('Se ha abierto algo!!', 0,
                                                                                       (255, 255, 255))
                    self.cyborg_texto_info_trampilla = self.ventana_juego.blit(self.cyborg_texto_info_trampilla,
                                                                           (1580, 950))

                    self.tiempo_mostrar_info_trampilla += 1

                else:
                    self.resetear_cyborg()

                    self.trampilla_descubierta = True
                    self.rejilla_abierta = True


        # ----------------------------------------------------------------------------------------------------------------
        # SALA DERECHA
        # ----------------------------------------------------------------------------------------------------------------

        if self.sala1_derecha:

            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_dcha.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            #self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if self.caja_voltaje and self.sala1_derecha and not self.sala1:

                self.alerta_voltaje = pygame.image.load("./imagenes/interior/peligro_electrico.png")
                self.alerta_voltaje = pygame.transform.scale(self.alerta_voltaje, (10, 8))
                self.alerta_voltaje = pygame.transform.rotate(self.alerta_voltaje, 48)
                self.alerta_voltaje = self.ventana_juego.blit(self.alerta_voltaje, (1493, 270))

            if self.bajar_escalera and not self.rejilla_abierta:
                # FONDO
                self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_dcha_rejilla.jpg")
                self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
                self.ventana_juego.blit(self.fondo1, (0, 0))

                if 0 <= self.tiempo_mostrar_info_rejilla <= 3:
                    self.cyborg_texto_info_bajar = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_bajar = self.cyborg_texto_info_bajar.render('Hay una rejilla cerrada', 0,
                                                                                       (255, 255, 255))
                    self.cyborg_texto_info_bajar = self.ventana_juego.blit(self.cyborg_texto_info_bajar,
                                                                           (1580, 950))

                    self.tiempo_mostrar_info_rejilla += 1

                else:
                    self.resetear_cyborg()

                    self.sala1_derecha = True
                    self.bajar_escalera = False

            if self.mirar_escalera_arriba and not self.cableado_activo:
                # FONDO
                self.fondo1 = pygame.image.load(
                    "./imagenes/interior/interior_1_dcha_cableado.jpg")
                self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
                self.ventana_juego.blit(self.fondo1, (0, 0))

                if 0 <= self.tiempo_mostrar_info_escalera_arriba <= 3:
                    self.cyborg_texto_info_escalera_arriba = pygame.font.Font(
                        "./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_escalera_arriba = self.cyborg_texto_info_escalera_arriba.render(
                        'La pantalla esta apagada', 0,
                        (255, 255, 255))
                    self.cyborg_texto_info_escalera_arriba = self.ventana_juego.blit(
                        self.cyborg_texto_info_escalera_arriba,
                        (1580, 950))

                    self.tiempo_mostrar_info_escalera_arriba += 1

                else:
                    self.resetear_cyborg()

                    self.mirar_escalera_arriba = False

        # ----------------------------------------------------------------------------------------------------------------
        # SALA DERECHA ESCALERAS
        # ----------------------------------------------------------------------------------------------------------------
        if self.sala1_derecha_escaleras and self.rejilla_abierta:
            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_dcha_escaleras.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if not self.cinta_encontrado:

                self.cinta = pygame.image.load("./imagenes/interior/cinta_adhesiva.png")
                self.cinta = pygame.transform.scale(self.cinta, (10, 15))
                # self.taza = pygame.transform.rotate(self.taza, 200)
                self.cinta = self.ventana_juego.blit(self.cinta, (1040, 690))

            else:

                # TIEMPO QUE SE MUESTRA LA IMAGEN EN GRANDE Y CENTRADA

                # cuando transcurran 2 segundos quitaremos la imagen del centro

                if 0 <= self.tiempo_mostrar_info_cinta <= 3:
                    self.cyborg_texto_info_cinta = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_cinta = self.cyborg_texto_info_cinta.render('Cinta adhesiva', 0,
                                                                                     (255, 255, 255))
                    self.cyborg_texto_info_cinta = self.ventana_juego.blit(self.cyborg_texto_info_cinta,
                                                                          (1580, 950))

                    self.tiempo_mostrar_info_cinta += 1

                else:
                    self.resetear_cyborg()

                    self.cinta_aumentada = False
                    self.sala1_derecha_escaleras = True

                if self.tiempo_mostrar_imagen == 2:

                    # mostramos el fondo inicial

                    # self.ventana_juego.blit(self.fondo1, (0, 0))

                    # Cambiamos el estado de la casilla que ocupara la imagen del objeto encontrado

                    self.casilla4_ocupada = True

                else:

                    # Mostramos la imagen del objeto encontardo en el centro durante 2 segundos

                    self.cinta_casillero = pygame.image.load("./imagenes/interior/cinta_adhesiva.png")
                    self.cinta_casillero = pygame.transform.scale(self.cinta_casillero, (300, 500))
                    # self.cinta_casillero = pygame.transform.rotate(self.cinta_casillero, 200)
                    self.cinta_casillero = self.ventana_juego.blit(self.cinta_casillero, (800, 185))

                    self.tiempo_mostrar_imagen += 1

        # ----------------------------------------------------------------------------------------------------------------
        # SALA DERECHA HACKER
        # ----------------------------------------------------------------------------------------------------------------
        if self.sala1_derecha_hacker:

            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_dcha_sala_hacker.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            #self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if not self.taza_encontrado:

                self.taza = pygame.image.load("./imagenes/interior/taza_termica_huella.png")
                self.taza = pygame.transform.scale(self.taza, (70, 110))
                #self.taza = pygame.transform.rotate(self.taza, 200)
                self.taza = self.ventana_juego.blit(self.taza, (1040, 690))

            else:

                # TIEMPO QUE SE MUESTRA LA IMAGEN EN GRANDE Y CENTRADA

                # cuando transcurran 2 segundos quitaremos la imagen del centro

                if 0 <= self.tiempo_mostrar_info_taza <= 3:
                    self.cyborg_texto_info_taza = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_taza = self.cyborg_texto_info_taza.render('La taza tiene una huella', 0,
                                                                                           (255, 255, 255))
                    self.cyborg_texto_info_taza = self.ventana_juego.blit(self.cyborg_texto_info_taza,
                                                                             (1580, 950))

                    self.tiempo_mostrar_info_taza += 1

                else:
                    self.resetear_cyborg()

                    self.taza_aumentada = False
                    self.sala1_derecha_hacker = True

                if self.tiempo_mostrar_imagen == 2:

                    # mostramos el fondo inicial

                    # self.ventana_juego.blit(self.fondo1, (0, 0))

                    # Cambiamos el estado de la casilla que ocupara la imagen del objeto encontrado

                    self.casilla3_ocupada = True

                else:

                    # Mostramos la imagen del objeto encontardo en el centro durante 2 segundos

                    self.taza_casillero = pygame.image.load("./imagenes/interior/taza_termica_huella.png")
                    self.taza_casillero = pygame.transform.scale(self.taza_casillero, (300, 500))
                    #self.taza_casillero = pygame.transform.rotate(self.taza_casillero, 200)
                    self.taza_casillero = self.ventana_juego.blit(self.taza_casillero, (800, 185))

                    self.tiempo_mostrar_imagen += 1

        # ----------------------------------------------------------------------------------------------------------------


        if self.caja_voltaje_aumentada:
            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_dcha_caja.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            if not self.voltaje_encontrado:

                self.voltaje = pygame.image.load("./imagenes/interior/anclaje_energia.png")
                self.voltaje = pygame.transform.scale(self.voltaje, (250, 160))
                self.voltaje = pygame.transform.rotate(self.voltaje, 200)
                self.voltaje = self.ventana_juego.blit(self.voltaje, (450, 560))

            else:

                # TIEMPO QUE SE MUESTRA LA IMAGEN EN GRANDE Y CENTRADA

                # cuando transcurran 2 segundos quitaremos la imagen del centro

                if 0 <= self.tiempo_mostrar_info_voltaje <= 3:
                    self.cyborg_texto_info_voltaje = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_voltaje = self.cyborg_texto_info_voltaje.render('Fuente de energia', 0,
                                                                                           (255, 255, 255))
                    self.cyborg_texto_info_voltaje = self.ventana_juego.blit(self.cyborg_texto_info_voltaje,
                                                                             (1580, 950))

                    self.tiempo_mostrar_info_voltaje += 1

                else:
                    self.resetear_cyborg()

                    self.caja_voltaje_aumentada = False
                    self.sala1_derecha = True

                if self.tiempo_mostrar_imagen == 2:

                    # mostramos el fondo inicial

                    # self.ventana_juego.blit(self.fondo1, (0, 0))

                    # Cambiamos el estado de la casilla que ocupara la imagen del objeto encontrado

                    self.casilla2_ocupada = True

                else:

                    # Mostramos la imagen del objeto encontardo en el centro durante 2 segundos

                    self.voltaje_casillero = pygame.image.load("./imagenes/interior/anclaje_energia.png")
                    self.voltaje_casillero = pygame.transform.scale(self.voltaje_casillero, (500, 500))
                    #self.voltaje_casillero = pygame.transform.rotate(self.voltaje_casillero, 200)
                    self.voltaje_casillero = self.ventana_juego.blit(self.voltaje_casillero, (700, 185))

                    self.tiempo_mostrar_imagen += 1

        # ----------------------------------------------------------------------------------------------------------------
        # SALA INTERMEDIA IZQUIERDA
        # ----------------------------------------------------------------------------------------------------------------

        if self.sala_intermedia_izquierda:

            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_intermedia_izqda.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if self.voltaje_usado:
                self.codigo = pygame.image.load("./imagenes/interior/codigo.png")
                self.codigo = pygame.transform.scale(self.codigo, (90, 40))
                self.codigo = pygame.transform.rotate(self.codigo, 357)
                self.codigo = self.ventana_juego.blit(self.codigo, (1520, 305))

            if self.huella_usada:
                self.huella_verde = pygame.image.load("./imagenes/interior/huella_verde.png")
                self.huella_verde = pygame.transform.scale(self.huella_verde, (50, 35))
                self.huella_verde = pygame.transform.rotate(self.huella_verde, 75)
                self.huella_verde = self.ventana_juego.blit(self.huella_verde, (440, 225))

        if self.mirar_caja_electrica and not self.electricidad_reestablecida:
            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_intermedia_izqda_caja_electrica.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_izquierda()
            self.resetear_cyborg()

            if self.voltaje_usado:
                self.voltaje = pygame.image.load("./imagenes/interior/anclaje_energia.png")
                self.voltaje = pygame.transform.scale(self.voltaje, (150, 100))
                self.voltaje = pygame.transform.rotate(self.voltaje, 130)
                self.voltaje = self.ventana_juego.blit(self.voltaje, (825, 495))

                self.codigo = pygame.image.load("./imagenes/interior/codigo.png")
                self.codigo = pygame.transform.scale(self.codigo, (350, 125))
                self.codigo = pygame.transform.rotate(self.codigo, 8)
                self.codigo = self.ventana_juego.blit(self.codigo, (750, 190))


                pygame.mixer_music.load("./musica/electricidad.mp3")
                pygame.mixer_music.play()


            if 0 <= self.tiempo_mostrar_info_caja_electrica <= 3:
                self.cyborg_texto_info_caja_electrica = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                self.cyborg_texto_info_caja_electrica = self.cyborg_texto_info_caja_electrica.render('No llega electricidad', 0,
                                                                                   (255, 255, 255))
                self.cyborg_texto_info_caja_electrica = self.ventana_juego.blit(self.cyborg_texto_info_caja_electrica,
                                                                       (1580, 950))

                self.tiempo_mostrar_info_caja_electrica += 1

            else:
                self.resetear_cyborg()

                #self.mirar_caja_electrica = False

        if self.mirar_lector_huellas and not self.lector_huellas_activado:
            # FONDO
            self.fondo1 = pygame.image.load(
                "./imagenes/interior/interior_1_intermedia_izqda_lector_huellas.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if self.huella_usada:

                self.huella_verde = pygame.image.load("./imagenes/interior/huella_verde.png")
                self.huella_verde = pygame.transform.scale(self.huella_verde, (350, 175))
                self.huella_verde = pygame.transform.rotate(self.huella_verde, 115)
                self.huella_verde = self.ventana_juego.blit(self.huella_verde, (785, 150))

                if self.cont == 0:
                    pygame.mixer_music.load("./musica/introduccion_1.mp3")
                    pygame.mixer_music.play()
                    self.cont += 1

            if 0 <= self.tiempo_mostrar_info_lector_huellas <= 3:
                self.cyborg_texto_info_lector_huellas = pygame.font.Font(
                    "./fuentes/JetBrainsMono-Regular.ttf", 13)
                self.cyborg_texto_info_lector_huellas = self.cyborg_texto_info_lector_huellas.render(
                    'Que es?, esta apagado', 0,
                    (255, 255, 255))
                self.cyborg_texto_info_lector_huellas = self.ventana_juego.blit(
                    self.cyborg_texto_info_lector_huellas,
                    (1580, 950))

                self.tiempo_mostrar_info_lector_huellas += 1

            else:
                self.resetear_cyborg()

                #self.mirar_lector_huellas = False


        # ----------------------------------------------------------------------------------------------------------------
        # SALA IZQUIERDA
        # ----------------------------------------------------------------------------------------------------------------

        if self.sala1_izquierda:
            
            # FONDO
            self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_izqda_puerta2.jpg")
            self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
            self.ventana_juego.blit(self.fondo1, (0, 0))

            self.resetear_flecha_derecha()
            self.resetear_cyborg()

            if not self.puerta_abierta:

                # TIEMPO QUE SE MUESTRA LA IMAGEN EN GRANDE Y CENTRADA

                # cuando transcurran 2 segundos quitaremos la imagen del centro

                if 0 <= self.tiempo_mostrar_info_puerta <= 3:
                    self.cyborg_texto_info_puerta = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                    self.cyborg_texto_info_puerta = self.cyborg_texto_info_puerta.render('La puerta esta cerrada', 0,
                                                                                           (255, 255, 255))
                    self.cyborg_texto_info_puerta = self.ventana_juego.blit(self.cyborg_texto_info_puerta,
                                                                             (1580, 950))

                    self.tiempo_mostrar_info_puerta += 1

                else:

                    self.resetear_cyborg()

            else:
                # FONDO
                self.fondo1 = pygame.image.load("./imagenes/interior/interior_1_izqda_puerta2_abierta.jpg")
                self.fondo1 = pygame.transform.scale(self.fondo1, (1920, 880))
                self.ventana_juego.blit(self.fondo1, (0, 0))

                if self.cont == 1:
                    pygame.mixer_music.load("./musica/puerta_final.mp3")
                    pygame.mixer_music.play()



        # ----------------------------------------------------------------------------------------------------------------
        # SUPEROBJETO
        # ----------------------------------------------------------------------------------------------------------------

        if self.mostrar_superobjeto:

            self.resetear_cyborg()

            # TIEMPO QUE SE MUESTRA LA IMAGEN EN GRANDE Y CENTRADA

            # cuando transcurran 2 segundos quitaremos la imagen del centro

            if 0 <= self.tiempo_mostrar_info_superobjeto <= 3:
                self.cyborg_texto_info_superobjeto = pygame.font.Font("./fuentes/JetBrainsMono-Regular.ttf", 13)
                self.cyborg_texto_info_superobjeto = self.cyborg_texto_info_superobjeto.render('Has extraído la huella', 0,
                                                                                   (255, 255, 255))
                self.cyborg_texto_info_superobjeto = self.ventana_juego.blit(self.cyborg_texto_info_superobjeto,
                                                                       (1580, 950))

                self.tiempo_mostrar_info_superobjeto += 1

            else:
                self.resetear_cyborg()

                self.superobjeto_aumentada = False


            if self.tiempo_mostrar_imagen == 2:

                # mostramos el fondo inicial

                # self.ventana_juego.blit(self.fondo1, (0, 0))

                # Cambiamos el estado de la casilla que ocupara la imagen del objeto encontrado

                self.casilla6_ocupada = True
                self.casilla3_ocupada = False
                self.casilla4_ocupada = False
                self.mostrar_superobjeto = False
            else:

                # Mostramos la imagen del objeto encontardo en el centro durante 2 segundos

                self.superobjeto_casillero = pygame.image.load("./imagenes/interior/cinta_adhesiva_huella.png")
                self.superobjeto_casillero = pygame.transform.scale(self.superobjeto_casillero, (300, 500))
                # self.superobjeto_casillero = pygame.transform.rotate(self.superobjeto_casillero, 200)
                self.superobjeto_casillero = self.ventana_juego.blit(self.superobjeto_casillero, (800, 185))

                self.tiempo_mostrar_imagen += 1



        # ----------------------------------------------------------------------------------------------------------------

        # GESTION DE LA CASILLA OCUPADA

        if self.casilla1_ocupada:
            # mostramos objeto encontrado en el interior de la casilla

            self.objeto1_encontrado = pygame.image.load("./imagenes/medallon.png")
            self.objeto1_encontrado = pygame.transform.scale(self.objeto1_encontrado, (50, 50))
            self.objeto1_encontrado = self.ventana_juego.blit(self.objeto1_encontrado, (40, 920))

        if self.casilla2_ocupada:
            self.voltaje_casillero = pygame.image.load("./imagenes/interior/anclaje_energia.png")
            self.voltaje_casillero = pygame.transform.scale(self.voltaje_casillero, (90, 90))
            #self.voltaje_casillero = pygame.transform.rotate(self.voltaje_casillero, 200)
            self.voltaje_casillero = self.ventana_juego.blit(self.voltaje_casillero, (250, 900))

        if self.casilla3_ocupada:
            self.taza_casillero = pygame.image.load("./imagenes/interior/taza_termica_huella.png")
            self.taza_casillero = pygame.transform.scale(self.taza_casillero, (40, 70))
            # self.taza_casillero = pygame.transform.rotate(self.taza_casillero, 200)
            self.taza_casillero = self.ventana_juego.blit(self.taza_casillero, (500, 910))

        if self.casilla4_ocupada:
            self.cinta_casillero = pygame.image.load("./imagenes/interior/cinta_adhesiva.png")
            self.cinta_casillero = pygame.transform.scale(self.cinta_casillero, (40, 70))
            # self.cinta_casillero = pygame.transform.rotate(self.cinta_casillero, 200)
            self.cinta_casillero = self.ventana_juego.blit(self.cinta_casillero, (720, 910))

        if self.casilla6_ocupada:
            self.cinta_casillero = pygame.image.load("./imagenes/interior/cinta_adhesiva_huella.png")
            self.cinta_casillero = pygame.transform.scale(self.cinta_casillero, (40, 70))
            # self.cinta_casillero = pygame.transform.rotate(self.cinta_casillero, 200)
            self.cinta_casillero = self.ventana_juego.blit(self.cinta_casillero, (1180, 910))

        # ----------------------------------------------------------------------------------------------------------------
        #SUPERFICIES TRANSPARENTES

        # PALANCA PUERTA

        self.surface_palanca = pygame.Surface((70, 100))  # the size of your rect
        # self.surface_palanca.set_alpha(50)  # alpha level 0  invisibility
        # self.surface_palanca.fill((255, 0, 0))  # this fills the entire surface
        # self.ventana_juego.blit(self.surface_palanca, (1310, 290))  # (0,0) are the top-left coordinates
        self.rect_palanca = self.surface_palanca.get_rect(topleft=(1310, 290))

        # CAJA VOLAJE
        self.surface_caja_voltaje = pygame.Surface((150, 150))  # the size of your rect
        # self.surface_caja_voltaje.set_alpha(50)  # alpha level 0  invisibility
        # self.surface_caja_voltaje.fill((255, 0, 0))  # this fills the entire surface
        # self.ventana_juego.blit(self.surface_caja_voltaje, (1475, 160))  # (0,0) are the top-left coordinates
        self.rect_caja_voltaje = self.surface_caja_voltaje.get_rect(topleft=(1475, 160))

        # SUBIR ESCALERA
        self.surface_escalera_arriba = pygame.Surface((375, 400))  # the size of your rect
        #self.surface_escalera_arriba.set_alpha(50)  # alpha level 0  invisibility
        #self.surface_escalera_arriba.fill((255, 0, 0))  # this fills the entire surface
        #self.ventana_juego.blit(self.surface_escalera_arriba, (775, 0))  # (0,0) are the top-left coordinates
        self.rect_escalera_arriba = self.surface_escalera_arriba.get_rect(topleft=(775, 0))

        # REJILLA ESCALERA
        self.surface_rejilla = pygame.Surface((375, 400))  # the size of your rect
        # self.surface_rejilla.set_alpha(50)  # alpha level 0  invisibility
        # self.surface_rejilla.fill((255, 0, 0))  # this fills the entire surface
        # self.ventana_juego.blit(self.surface_rejilla, (775, 400))  # (0,0) are the top-left coordinates
        self.rect_rejilla = self.surface_rejilla.get_rect(topleft=(775, 400))

        '''
        # PUERTA SALA 1 IZQUIERDA
        self.surface_puerta = pygame.Surface((740, 850))  # the size of your rect
        self.surface_puerta.set_alpha(50)  # alpha level 0  invisibility
        self.surface_puerta.fill((255, 0, 0))  # this fills the entire surface
        self.ventana_juego.blit(self.surface_puerta, (600, 10))  # (0,0) are the top-left coordinates
        self.rect_puerta = self.surface_puerta.get_rect(topleft=(600, 10))
        
        '''
        # PUERTA2 SALA 1 IZQUIERDA
        self.surface_puerta = pygame.Surface((340, 320))  # the size of your rect
        #self.surface_puerta.set_alpha(50)  # alpha level 0  invisibility
        #self.surface_puerta.fill((255, 0, 0))  # this fills the entire surface
        #self.ventana_juego.blit(self.surface_puerta, (700, 370))  # (0,0) are the top-left coordinates
        self.rect_puerta = self.surface_puerta.get_rect(topleft=(700, 370))

        # PERSIANA SALA INTERMEDIA DERECHA
        self.surface_persiana = pygame.Surface((275, 220))  # the size of your rect
        #self.surface_persiana.set_alpha(50)  # alpha level 0  invisibility
        #self.surface_persiana.fill((255, 0, 0))  # this fills the entire surface
        #self.ventana_juego.blit(self.surface_persiana, (1000, 458))  # (0,0) are the top-left coordinates
        self.rect_persiana = self.surface_persiana.get_rect(topleft=(1000, 458))


        # TRAMPILLA SALA INTERMEDIA DERECHA
        self.surface_trampilla = pygame.Surface((50, 15))  # the size of your rect
        #self.surface_trampilla.set_alpha(50)  # alpha level 0  invisibility
        #self.surface_trampilla.fill((255, 0, 0))  # this fills the entire surface
        #self.ventana_juego.blit(self.surface_trampilla, (420, 760))  # (0,0) are the top-left coordinates
        self.rect_trampilla = self.surface_trampilla.get_rect(topleft=(420, 760))

        # CAJA ELECTRICA SALA INTERMEDIA IZQUIERDA
        self.surface_caja_electrica = pygame.Surface((120, 110))  # the size of your rect
        #self.surface_caja_electrica.set_alpha(50)  # alpha level 0  invisibility
        #self.surface_caja_electrica.fill((255, 0, 0))  # this fills the entire surface
        #self.ventana_juego.blit(self.surface_caja_electrica, (1520, 400))  # (0,0) are the top-left coordinates
        self.rect_caja_electrica = self.surface_caja_electrica.get_rect(topleft=(1520, 400))

        # LECTOR HUELLAS SALA INTERMEDIA IZQUIERDA
        self.surface_lector_huellas = pygame.Surface((120, 70))  # the size of your rect
        #self.surface_lector_huellas.set_alpha(50)  # alpha level 0  invisibility
        #self.surface_lector_huellas.fill((255, 0, 0))  # this fills the entire surface
        #self.ventana_juego.blit(self.surface_lector_huellas, (400, 220))  # (0,0) are the top-left coordinates
        self.rect_caja_lector_huellas = self.surface_lector_huellas.get_rect(topleft=(400, 220))

    def resetear_cyborg(self):
        self.cyborg = pygame.image.load("./imagenes/cyborg.jpg")
        self.cyborg = pygame.transform.scale(self.cyborg, (400, 150))
        self.cyborg = self.ventana_juego.blit(self.cyborg, (1450, 880))

    def resetear_flecha_derecha(self):
        # FLECHAS DE CONTROL
        self.flecha_derecha = pygame.image.load("./imagenes/flecha_dcha.png")
        self.flecha_derecha = pygame.transform.scale(self.flecha_derecha, (100, 150))
        self.flecha_derecha = self.ventana_juego.blit(self.flecha_derecha, (1800, 350))

    def resetear_flecha_izquierda(self):
        self.flecha_izquierda = pygame.image.load("./imagenes/flecha_izqda.png")
        self.flecha_izquierda = pygame.transform.scale(self.flecha_izquierda, (100, 150))
        self.flecha_izquierda = self.ventana_juego.blit(self.flecha_izquierda, (20, 350))