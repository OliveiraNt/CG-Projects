secondRadius, minuteRadius, hoursRadius, clockDiameter = 0.0, 0.0, 0.0, 0.0
cx, cy = 0, 0
c1 = color(random(255), random(255), random(255))
c2 = color(random(255), random(255), random(255))
def setup():
    
    size(640,360)
    stroke(255)
    
    global secondRadius
    global minuteRadius
    global hoursRadius
    global clockDiameter
    global cx
    global cy
    
    radius = min(width, height) / 2
    secondRadius = radius * 0.72
    minuteRadius = radius * 0.60
    hoursRadius = radius * 0.50
    clockDiameter = radius * 1.8
    
    cx = width / 2
    cy = height / 2
    
def draw():
    background(0)
    
    fill(c1)
    noStroke()
    ellipse(cx, cy, clockDiameter, clockDiameter)
    
    s = map(second(), 0, 60, 0, TWO_PI) - HALF_PI
    m = map(minute() + norm(second(), 0, 60), 0, 60, 0, TWO_PI) - HALF_PI
    h = map(hour() + norm(minute(), 0, 60), 0, 24, 0, TWO_PI * 2) - HALF_PI
    
    stroke(c2)
    strokeWeight(1)
    line(cx, cy, cx + cos(s) * secondRadius, cy + sin(s) * secondRadius)
    strokeWeight(2)
    line(cx, cy, cx + cos(m) * minuteRadius, cy + sin(m) * minuteRadius)
    strokeWeight(4)
    line(cx, cy, cx + cos(h) * hoursRadius, cy + sin(h) * hoursRadius)
    
    