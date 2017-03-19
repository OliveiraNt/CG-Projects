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

def koch_snowflake(ax, ay, bx, by, n, k):

    if n == 4:
        line(ax, ay, bx, by)
    else:
        ax2 = 2*ax/3 + bx/3
        ay2 = 2*ay/3 + by/3
        
        bx2 = ax/3 + 2*bx/3
        by2 = ay/3 + 2*by/3
        if k == 0:
            r = make_rotation(ax2,ay2,bx2,by2,PI/3)
        else:
            r = make_rotation(ax2,ay2,bx2,by2,-PI/3)
        rx = r[0]
        ry = r[1]
        
        koch_snowflake(ax,ay,ax2,ay2,n+1,k)
        koch_snowflake(ax2,ay2,rx,ry,n+1,k)
        koch_snowflake(rx,ry,bx2,by2,n+1,k)
        koch_snowflake(bx2,by2,bx,by,n+1,k)
    
    
        
def draw():
    
    background(0)
    stroke(255)
    ax, ay, bx, by = 200, 200,400,200
    e = make_rotation(ax,ay,bx,by,-PI/3)
    ex = e[0]
    ey = e[1]

    koch_snowflake(ax, ay, bx, by, 0, 0)
    koch_snowflake(ax, ay, ex, ey, 0, 1)
    koch_snowflake(bx, by, ex, ey, 0, 0)