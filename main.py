import pygame as pg

taxiSprite=pg.image.load("Assets/taxi.png")

class Game:
    def __init__(self):
        pg.init()
        self.display=pg.display.set_mode((1000, 800))
        pg.display.set_caption("Taxi Game")

        self.taxiX=400
        self.taxiY=300

        self.carSpeedX=0
        self.carSpeedY=0
        self.angle=180

        self.turnSpeed=3
        self.maxSpeed=25
        self.acceleration=2
        self.drag=2

        self.taxi=0

    def draw(self):
            self.display.fill("darkslategray")
        

    def run(self):
        while (True):
            self.draw()
            self.handleInput()
            self.handleTaxi()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

    def handleInput(self):
        key=pg.key.get_pressed()

        if key[pg.K_a]:
            self.angle+=self.turnSpeed

        if key[pg.K_d]:
            self.angle-=self.turnSpeed

        

    def handleTaxi(self):
        #self.carSpeedY-=self.drag
        self.taxi=pg.transform.rotate(taxiSprite,self.angle)
        self.display.blit(self.taxi,(self.taxiX,self.taxiY))


        


if __name__ == "__main__":
    app = Game()
    app.run()