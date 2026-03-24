from pygame import *
init()

#CONSTANTES
WIDTH, HEIGHT = 640, 480
TITLE = 'Project Labby'
BACK_COL = (45, 78, 105)
BLACK = (0,0,0)
WHITE = (255,255,255)
PLAYER_IMG = 'pac-1.png'
PLAYER_IMG2 = 'pixil.png'

# GUI
pantalla = display.set_mode((WIDTH, HEIGHT))
display.set_caption(TITLE)

#Clase Madre
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed = 0):
        #LLAMAR AL METODO CONSTRUCTOR DE LA MAMA
        super().__init__()
        #Carga y establece la imagen
        self.image = transform.scale(image.load(img), (100, 100))
        #CREAR UN RECTANGULO PARA EL OBJETO (Marco)
        self.rect = self.image.get_rect()
        self.rectX = x
        self.rectY = y
        self.speed = speed

#Metodo para renderizar en pantalla
    def reset(self):
        pantalla.blit(self.image, (self.rectX, self.rectY))

#Crear objetos (instancias)
player = GameSprite(PLAYER_IMG, 200, 200, 5)
player2 = GameSprite(PLAYER_IMG2, 100, 100, 5)

#CICLO DEL JUEGO
run = True
clock = time.Clock()


while run:
    #Eventos
    for e in event.get():
        if e.type == QUIT:
            run = False

    pantalla.fill(BACK_COL)
    player.reset()
    player2.reset()
    display.update()

display.update()

quit()