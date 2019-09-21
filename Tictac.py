import pygame,sys
from pygame.locals import *
from Dib import Dib

enJuego=True


Tablerosup=[]
Tableromid=[]
Tablerolow=[]
#Comentario de prueba2.0
#Agregue otro comentario nuevo
def DibujarTablero(superficie,Turno):
    mifuente= pygame.font.SysFont("Arial",25)
    Texto1= mifuente.render("Turno del jugador 1",30,(0,0,0))
    Texto2= mifuente.render("Turno del jugador 2",30,(0,0,0))

    tercio = 800/3
    superficie.fill((255,255,255))

    if Turno==1:
        superficie.blit(Texto1,(200,800))
    if Turno==2:
        superficie.blit(Texto2,(200,800))

    #Verticales
    pygame.draw.line(superficie,(0,0,0),(tercio,0),(tercio,800),5)
    pygame.draw.line(superficie,(0,0,0),((tercio*2),0),((tercio*2),800),5)
    pygame.draw.line(superficie,(0,0,0),((tercio*3),0),((tercio*3),800),5)
    #Horizontales
    pygame.draw.line(superficie,(0,0,0),(0,tercio),(800,tercio),5)
    pygame.draw.line(superficie,(0,0,0),(0,tercio*2),(800,tercio*2),5)
    pygame.draw.line(superficie,(0,0,0),(0,tercio*3),(800,tercio*3),5)
    for dibu in Tablerosup:
        dibu.dibujar(superficie)
    for dibu in Tableromid:
        dibu.dibujar(superficie)
    for dibu in Tablerolow:
        dibu.dibujar(superficie)


def llenarTablero():
    tercio =800/3
    sexto = 800/6
    
    #TableroSup
    Dibujo1 = Dib(0,0)
    Dibujo2 = Dib(tercio,0)
    Dibujo3 = Dib((tercio*2),0)

    Tablerosup.append(Dibujo1)
    Tablerosup.append(Dibujo2)
    Tablerosup.append(Dibujo3)

    #TableroMid
    Dibujo4 = Dib(0,tercio)
    Dibujo5 = Dib(tercio,tercio)
    Dibujo6 = Dib((tercio*2),tercio)

    Tableromid.append(Dibujo4)
    Tableromid.append(Dibujo5)
    Tableromid.append(Dibujo6)

    #TableroLow
    Dibujo7 = Dib(0,(tercio*2))
    Dibujo8 = Dib(tercio,(tercio*2))
    Dibujo9 = Dib((tercio*2),(tercio*2))

    Tablerolow.append(Dibujo7)
    Tablerolow.append(Dibujo8)
    Tablerolow.append(Dibujo9)

def ganador(): 

    global enJuego    
    cerocero = Tablerosup[0]
    cerouno = Tablerosup[1]
    cerodos = Tablerosup[2]
    unocero = Tableromid[0]
    unouno = Tableromid[1]
    unodos = Tableromid[2]
    doscero = Tablerolow[0]
    dosuno = Tablerolow[1]
    dosdos = Tablerolow[2]
    #Chequeos del primer jugador
    #---------------------------------------------------------------------------------------------------
    #diagonal izqlow-dersup
    if doscero.getPlayer()==1 and unouno.getPlayer()==1 and cerodos.getPlayer()==1:
        enJuego=False
        return 1
    #diagonal izqsup-derlow
    if cerocero.getPlayer()==1 and unouno.getPlayer()==1 and dosdos.getPlayer()==1:
        enJuego=False
        return 1
    #filas
    if cerocero.getPlayer()==1 and cerouno.getPlayer()==1 and cerodos.getPlayer()==1:
        enJuego=False
        return 1
    if unocero.getPlayer()==1 and unouno.getPlayer()==1 and unodos.getPlayer()==1:
        enJuego=False
        return 1
    if doscero.getPlayer()==1 and dosuno.getPlayer()==1 and dosdos.getPlayer()==1:
        enJuego=False
        return 1
    
    if cerocero.getPlayer()==1 and unocero.getPlayer()==1 and doscero.getPlayer()==1:
        enJuego =False
        return 1
    if cerouno.getPlayer()==1 and unouno.getPlayer()==1 and dosuno.getPlayer()==1:
        enJuego=False
        return 1
    if cerodos.getPlayer()==1 and unodos.getPlayer()==1 and dosdos.getPlayer()==1:
        enJuego =False
        return 1
    #-------------------------------------------------------------------------------------------
    #Chequeos del segundo jugador
    if doscero.getPlayer()==2 and unouno.getPlayer()==2 and cerodos.getPlayer()==2:
        enJuego=False
        return 2
    #diagonal izqsup-derlow
    if cerocero.getPlayer()==2 and unouno.getPlayer()==2 and dosdos.getPlayer()==2:
        enJuego=False
        return 2
    #filas
    if cerocero.getPlayer()==2 and cerouno.getPlayer()==2 and cerodos.getPlayer()==2:
        enJuego=False
        return 2
    if unocero.getPlayer()==2 and unouno.getPlayer()==2 and unodos.getPlayer()==2:
        enJuego=False
        return 2
    if doscero.getPlayer()==2 and dosuno.getPlayer()==2 and dosdos.getPlayer()==2:
        enJuego=False
        return 2
    
    if cerocero.getPlayer()==2 and unocero.getPlayer()==2 and doscero.getPlayer()==2:
        enJuego =False
        return 2
    if cerouno.getPlayer()==2 and unouno.getPlayer()==2 and dosuno.getPlayer()==2:
        enJuego=False
        return 2
    if cerodos.getPlayer()==2 and unodos.getPlayer()==2 and dosdos.getPlayer()==2:
        enJuego =False
        return 2

    
    


def IniciarJuego():
    pygame.init()
    ventana = pygame.display.set_mode((800,840))
    pygame.display.set_caption("Tic tac toe")
    ventana.fill((255,255,255))
    mifuente= pygame.font.SysFont("Arial",40)
    TextoGanador1= mifuente.render("EL GANADOR ES EL JUGADOR 1",30,(255,0,0),(255,255,255))
    TextoGanador2= mifuente.render("EL GANADOR ES EL JUGADOR 2",30,(255,0,0),(255,255,255))

    llenarTablero()
    
    p1=1
    p2=2
    Turno=p1


    while enJuego:
        
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            if enJuego==True:

                #jugador 1 se chequea las posiciones
                if Turno==p1:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:  # Left mouse button.
                            #parte de abajo del tablero
                            for dib in Tablerolow:
                                if not dib.getClick():
                                    dib.chequear_click(event.pos,p1)
                                    if dib.getPlayer()==1:
                                        print("entro caso 1")
                                        Turno=2
                                    
                            #parte media
                            for dib in Tableromid:
                                if not dib.getClick():
                                    dib.chequear_click(event.pos,p1)
                                    if dib.getPlayer()==1:
                                        print("entro caso 2")
                                        Turno=2

                            #parte superior
                            for dib in Tablerosup:
                                if not dib.getClick():
                                    dib.chequear_click(event.pos,p1)
                                    if dib.getPlayer()==1:
                                        print("entro caso 3")
                                        Turno=2

                #jugador 2 se chequean las posiciones
                if Turno==p2:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:  # Left mouse button.

                            #parte de abajo del tablero
                            for dib in Tablerolow:
                                if not dib.getClick():
                                    dib.chequear_click(event.pos,p2)
                    
                                    if dib.getPlayer()==2:
                                        print("entro caso 4")
                                        Turno=1
                                   
                                    
                            #parte media
                            for dib in Tableromid:
                                if not dib.getClick():
                                    dib.chequear_click(event.pos,p2)
                                
                                    if dib.getPlayer()==2:
                                        print("entro caso 5")
                                        Turno=1

                            #parte superior
                            for dib in Tablerosup:
                                if not dib.getClick():
                                    dib.chequear_click(event.pos,p2)

                                    if dib.getPlayer()==2:
                                        print("entro caso 6")
                                        Turno=1
        DibujarTablero(ventana,Turno)
        ganador()
        if ganador() ==1:
            ventana.blit(TextoGanador1,(100,400))
        if ganador() ==2:
            ventana.blit(TextoGanador2,(100,400))

                    
        
        pygame.display.flip()
    
    print("Fin del juego")

    while not enJuego:
        DibujarTablero(ventana,Turno)
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            






IniciarJuego()