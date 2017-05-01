a, b, c = -1, -3, 0

def setup():
    
    size(500, 500)
    
def draw_root ():
    
    delta = (b ** 2) - (4 * a * c)
        
    min_max = []
        
    x1 = ((-b) + sqrt(delta))/(2 * a)
    x2 = ((-b) - sqrt(delta))/(2 * a)
    
    aux = - b /(2.0 * a)
        
    min_max.append(aux)
        
    aux = y(a, b, c, min_max[0])
    min_max.append(aux)
    
    root1 = _scale(6, 6, x1, 0)
    root2 = _scale(6, 6, x2, 0)
    min_max = _scale(6, 6, min_max[0], min_max[1])
        
    strokeWeight(5)
    stroke(0)
    point(root1[0], root1[1])
    point(root2[0], root2[1])
    point(min_max[0], min_max[1])
    
def y(a, b, c, x):
    
    return (a * (x ** 2)) + (b * x) + c
    
def _scale(wx, wy, x, y):
    
    xs = (width/2) + ((width * x)/wx)
    ys = (height/2) - ((height * y)/wy)
    
    return [xs, ys]

def draw_parabola(x, xf):

    noFill()
    strokeWeight(1)
    stroke(252, 8, 8)
    beginShape()
    
    while x < xf:
        xy = _scale(6, 6, x, y(a, b, c, x))
        vertex(xy[0], xy[1])
        x += 0.01
        
    endShape()
    
def draw():
    
    strokeWeight(1)
    line(width/2, 0, width/2, height)
    line(0, height/2, width, height/2)
    draw_parabola(-3, 3)
    draw_root()
    