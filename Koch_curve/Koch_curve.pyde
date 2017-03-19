def setup():
    size(640, 400)
    
    
def make_rotation(px, py, qx, qy, theta):
    p2x = px - qx
    p2y = py - qy
    p3x = p2x * cos(theta) + p2y * sin(theta)
    p3y = p2y * cos(theta) - p2x * sin(theta)
    p3x += qx
    p3y += qy
    
    e = (p3x, p3y)
    return e

def magic(ax, ay, bx, by, n):
    
    if n == 4:
        line(ax, ay, bx, by)
    
    else:
        cx = 2*ax/3 + bx/3
        cy = 2*ay/3 + by/3
        
        dx = ax/3 + 2*bx/3
        dy = ay/3 + 2*by/3
    
        e = make_rotation(cx,cy,dx,dy,-PI/3)
        ex = e[0]
        ey = e[1]
        
        magic(ax,ay,cx,cy,n+1)
        magic(cx,cy,ex,ey,n+1)
        magic(ex,ey,dx,dy,n+1)
        magic(dx,dy,bx,by,n+1)
        
def draw():
    
    background(0)
    stroke(255)
    magic(20, 200, 620, 200, 0)
