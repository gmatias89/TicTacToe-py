import pygame,sys
from pygame.locals import *
from Dib import Dib
#Jugador 1 y 2
p1=1
p2=2

Tablerosup=[]
Tableromid=[]
Tablerolow=[]
#Comentario de prueba2.0
#Agregue otro comentario nuevo
def DibujarTablero(superficie):
    tercio = 800/3
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

def IniciarJuego():
    pygame.init()
    ventana = pygame.display.set_mode((800,840))
    pygame.display.set_caption("Tic tac toe")
    ventana.fill((255,255,255))
    mifuente= pygame.font.SysFont("Arial",25)
    Texto1= mifuente.render("Turno del jugador 1",30,(0,0,0))
    Texto2= mifuente.render("Turno del jugador 1",30,(0,0,0))
    llenarTablero()
    enJuego=True
    Turno=p1

    while True:
        
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
        #while Turno==p1:
           # ventana.blit(Texto1,(200,850))

        
                    
        ventana.blit(Texto1,(270,800))
        DibujarTablero(ventana)
        pygame.display.flip()
    
            






IniciarJuego()