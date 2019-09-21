import pygame


class Dib(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.imagen1= pygame.image.load("TicTacToe/Imagenes/cruz.png")
        self.imagen2= pygame.image.load("TicTacToe/Imagenes/circulo.png")
        self.imagen0= pygame.image.load("TicTacToe/Imagenes/vacio.png")

        self.player=0
        self.listaImagenes=[self.imagen0,self.imagen1,self.imagen2]
        self.imagenDibujo=self.listaImagenes[self.player]

        self.posx=x
        self.posy=y
        self.rect=self.imagenDibujo.get_rect()
        self.rect.top=self.posy
        self.rect.left=self.posx

        
        self.click=False
    
    def chequear_click(self,evento,player):
        if self.rect.collidepoint(evento):
            self.clicked(player)


    def getClick(self):
        return self.click
    
    def getPlayer(self):
        return self.player
        
    def dibujar(self,superficie):
        self.imagenDibujo=self.listaImagenes[self.player]
        superficie.blit(self.imagenDibujo,self.rect)
    
    def clicked(self,jugador):
        if self.click==False:
            self.click=True
            self.player=jugador
            self.imagenDibujo=self.listaImagenes[jugador]
            





