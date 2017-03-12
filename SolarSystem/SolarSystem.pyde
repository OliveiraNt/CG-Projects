from Planet import Planet

sun = None
earth = None
def setup():
    size(600, 600)
    global sun
    sun = Planet(50, 0, 0)
    sun.spawnMoons(1, 1)
    
def draw():
    background(0)
    translate(width/2, height/2)
    sun.show()
    sun.orbit()
    
    