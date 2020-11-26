# imortamos librerias systema y gestion de juegos
import pygame
import escape_room
import menu
import menu2
import prologo


def main():
    '''
    menu_juego = menu.Menu()
    menu_juego.opciones()
    '''


    menu_juego2 = menu2.Menu()
    menu_juego2.opciones()

    pygame.time.wait(500)

    comenzar_prologo = prologo.Prologo()
    comenzar_prologo.pantallas()

    pygame.time.wait(500)

    juego_scape = escape_room.EscapeRoom()
    juego_scape.juego()


if __name__ == '__main__':
    # iniciamos juego

    pygame.init()
    main()

