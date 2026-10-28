import pygame as pg

taxiSprite=pg.image.load("Assets/taxi.png")

class Game:
    def __init__(self):
        pg.init
        self.display=pg.display.set_mode((800, 600))
        pg.display.set_caption("Taxi Game")

        self.taxiX=400
        self.taxiY=300

        self.carSpeedX=0
        self.carSpeedY=0

        self.maxSpeed=25

        self.drag=2

    def draw(self):
        self.display.blit(taxiSprite,(self.taxiX,self.taxiY))
        

    def run(self):
        while (True):
            pg.display.flip()
            self.getInput()
            self.handleTaxi()
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

    def getInput(self):
        return pg.key.get_pressed()

    def handleTaxi(self):
        key=self.getInput()

        if (key==pg.K_w):
            if (self.carSpeedY+5>self.maxSpeed):
                self.carSpeedY+(abs(5-self.carSpeedY))
                self.taxiq+=self.carSpeedY

        


if __name__ == "__main__":
    app = Game()
    app.run()