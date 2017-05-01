class Planet(object):
    
    def __init__(self, r, d, o):
        self.radius = r
        self.distance = d
        self.angle = random(TWO_PI)
        self.orbitspeed = o
        self.planets = []
        self.c = color(random(0, 255), random(0, 255), random(0, 255))

    def orbit(self):
        self.angle = self.angle + self.orbitspeed
        if self.planets:
            for i in range(len(self.planets)):
                self.planets[i].orbit()

    def spawnMoons(self, total, level):
        self.planets = []
        for i in range(total):
            self.r = self.radius/(level*2)
            self.d = random(30, 50) + self.radius*2
            self.o = random(-0.05, 0.05)
            self.p = Planet(self.r, self.d/level, self.o)
            self.planets.append(self.p)
            if level < 2:
                for i in range(len(self.planets)):
                    self.num = 1
                    self.planets[i].spawnMoons(self.num, level+1)
                                  
        
    def show(self):
        pushMatrix()
        fill(self.c)
        rotate(self.angle)
        translate(self.distance, 0)
        ellipse(0, 0, self.radius*2,self.radius*2)
        if self.planets:
            for i in range(len(self.planets)):
                self.planets[i].show()
        
        popMatrix()