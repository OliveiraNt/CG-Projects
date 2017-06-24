class Cube :
	
  def __init__(self, center, a, config):

    self.color = ((1,1,0),(1,1,1),(0,0,1),(1.0,0.5,0.0),(0,1,0),(1,0,0))
 
    self.vertex = ((center[0]+a/2.0, center[1]+a/2.0, center[2]-a/2.0),
                   (center[0]+a/2.0, center[1]-a/2.0, center[2]-a/2.0),
                   (center[0]-a/2.0, center[1]-a/2.0, center[2]-a/2.0),
                   (center[0]-a/2.0, center[1]+a/2.0, center[2]-a/2.0),
                   (center[0]+a/2.0, center[1]+a/2.0, center[2]+a/2.0),
                   (center[0]+a/2.0, center[1]-a/2.0, center[2]+a/2.0),
                   (center[0]-a/2.0, center[1]-a/2.0, center[2]+a/2.0),
                   (center[0]-a/2.0, center[1]+a/2.0, center[2]+a/2.0))
		
    if config == 'rw':
		  self.faces = (((0,3,7,4),self.color[5]),    #red     - 5
                    ((4,5,6,7),self.color[1]),    #White   - 1
                    ((2,6,7,3),self.color[4]),    
                    ((0,1,2,3),self.color[0]),    
                    ((0,1,5,4),self.color[2]),    
                    ((1,2,6,5),self.color[3]))    
    if config == 'rb':
		  self.faces = (((0,3,7,4),self.color[5]),    #red     - 5
                    ((4,5,6,7),self.color[2]),    #blue    - 2
                    ((2,6,7,3),self.color[1]),    
                    ((0,1,2,3),self.color[4]),    
                    ((0,1,5,4),self.color[0]),    
                    ((1,2,6,5),self.color[3]))    
    if config == 'ry':
		  self.faces = (((0,3,7,4),self.color[5]),    #red     - 5
                    ((4,5,6,7),self.color[0]),    #yellow  - 0
                    ((2,6,7,3),self.color[2]),    
                    ((0,1,2,3),self.color[1]),    
                    ((0,1,5,4),self.color[4]),    
                    ((1,2,6,5),self.color[3]))    
    if config == 'rg':
		  self.faces = (((0,3,7,4),self.color[5]),    #red     - 5
                    ((4,5,6,7),self.color[4]),    #green   - 4
                    ((2,6,7,3),self.color[0]),    
                    ((0,1,2,3),self.color[2]),    
                    ((0,1,5,4),self.color[1]),    
                    ((1,2,6,5),self.color[3]))    
    if config == 'yr':
		  self.faces = (((0,3,7,4),self.color[0]),    #yellow  - 0
                    ((4,5,6,7),self.color[5]),    #red     - 5
                    ((2,6,7,3),self.color[4]),    
                    ((0,1,2,3),self.color[3]),    
                    ((0,1,5,4),self.color[2]),    
                    ((1,2,6,5),self.color[1]))    
    if config == 'yb':
		  self.faces = (((0,3,7,4),self.color[0]),    #yellow  - 0
                    ((4,5,6,7),self.color[2]),    #blue    - 2
                    ((2,6,7,3),self.color[5]),    
                    ((0,1,2,3),self.color[4]),    
                    ((0,1,5,4),self.color[3]),    
                    ((1,2,6,5),self.color[1]))    
    if config == 'yo':
		  self.faces = (((0,3,7,4),self.color[0]),    #yellow  - 0
                    ((4,5,6,7),self.color[3]),    #orange  - 3
                    ((2,6,7,3),self.color[2]),    
                    ((0,1,2,3),self.color[5]),    
                    ((0,1,5,4),self.color[4]),    
                    ((1,2,6,5),self.color[1]))    
    if config == 'yg':
		  self.faces = (((0,3,7,4),self.color[0]),    #yellow  - 0
                    ((4,5,6,7),self.color[4]),    #green   - 4
                    ((2,6,7,3),self.color[3]),    
                    ((0,1,2,3),self.color[2]),    
                    ((0,1,5,4),self.color[5]),    
                    ((1,2,6,5),self.color[1]))    
    if config == 'gw':
		  self.faces = (((0,3,7,4),self.color[4]),    #green   - 4
                    ((4,5,6,7),self.color[1]),    #White   - 1
                    ((2,6,7,3),self.color[3]),    
                    ((0,1,2,3),self.color[0]),    
                    ((0,1,5,4),self.color[5]),    
                    ((1,2,6,5),self.color[2]))    
    if config == 'gr':
		  self.faces = (((0,3,7,4),self.color[4]),    #green   - 4
                    ((4,5,6,7),self.color[5]),    #red     - 5
                    ((2,6,7,3),self.color[1]),    
                    ((0,1,2,3),self.color[3]),    
                    ((0,1,5,4),self.color[0]),    
                    ((1,2,6,5),self.color[2]))    
    if config == 'gy':
		  self.faces = (((0,3,7,4),self.color[4]),    #green   - 4
                    ((4,5,6,7),self.color[0]),    #yellow  - 0
                    ((2,6,7,3),self.color[5]),    
                    ((0,1,2,3),self.color[1]),    
                    ((0,1,5,4),self.color[3]),    
                    ((1,2,6,5),self.color[2]))    
    if config == 'go':
		  self.faces = (((0,3,7,4),self.color[4]),    #green   - 4
                    ((4,5,6,7),self.color[3]),    #orange  - 3
                    ((2,6,7,3),self.color[0]),    
                    ((0,1,2,3),self.color[5]),    
                    ((0,1,5,4),self.color[1]),    
                    ((1,2,6,5),self.color[2]))    
    if config == 'ow':
		  self.faces = (((0,3,7,4),self.color[3]),    #orange  - 3
                    ((4,5,6,7),self.color[1]),    #White   - 1
                    ((2,6,7,3),self.color[2]),    
                    ((0,1,2,3),self.color[0]),    
                    ((0,1,5,4),self.color[4]),    
                    ((1,2,6,5),self.color[5]))    
    if config == 'og':
		  self.faces = (((0,3,7,4),self.color[3]),    #orange  - 3
                    ((4,5,6,7),self.color[4]),    #green   - 4
                    ((2,6,7,3),self.color[1]),    
                    ((0,1,2,3),self.color[2]),    
                    ((0,1,5,4),self.color[0]),    
                    ((1,2,6,5),self.color[5]))    
  
    if config == 'oy':
		  self.faces = (((0,3,7,4),self.color[3]),    #orange  - 3
                    ((4,5,6,7),self.color[0]),    #yellow  - 0
                    ((2,6,7,3),self.color[4]),    
                    ((0,1,2,3),self.color[1]),    
                    ((0,1,5,4),self.color[2]),    
                    ((1,2,6,5),self.color[5]))    
    if config == 'ob':
		  self.faces = (((0,3,7,4),self.color[3]),    #orange  - 3
                    ((4,5,6,7),self.color[2]),    #blue    - 2
                    ((2,6,7,3),self.color[4]),    
                    ((0,1,2,3),self.color[1]),    
                    ((0,1,5,4),self.color[0]),    
                    ((1,2,6,5),self.color[5]))  
    if config == 'wr':
		  self.faces = (((0,3,7,4),self.color[1]),    #White   - 1
                    ((4,5,6,7),self.color[5]),    #red     - 5
                    ((2,6,7,3),self.color[2]),    
                    ((0,1,2,3),self.color[3]),    
                    ((0,1,5,4),self.color[4]),    
                    ((1,2,6,5),self.color[0]))    
    if config == 'wg':
		  self.faces = (((0,3,7,4),self.color[1]),    #White   - 1
                    ((4,5,6,7),self.color[4]),    #green   - 4
                    ((2,6,7,3),self.color[5]),    
                    ((0,1,2,3),self.color[2]),    
                    ((0,1,5,4),self.color[3]),    
                    ((1,2,6,5),self.color[0]))  
   
    if config == 'wo':
		  self.faces = (((0,3,7,4),self.color[1]),    #White   - 1
                    ((4,5,6,7),self.color[3]),    #orange  - 3
                    ((2,6,7,3),self.color[4]),    
                    ((0,1,2,3),self.color[5]),    
                    ((0,1,5,4),self.color[2]),    
                    ((1,2,6,5),self.color[0]))    
    if config == 'wb':
		  self.faces = (((0,3,7,4),self.color[1]),    #White   - 1
                    ((4,5,6,7),self.color[2]),    #blue    - 2
                    ((2,6,7,3),self.color[3]),    
                    ((0,1,2,3),self.color[4]),    
                    ((0,1,5,4),self.color[5]),    
                    ((1,2,6,5),self.color[0])) 
  
    if config == 'bw':
		  self.faces = (((0,3,7,4),self.color[2]),    #blue    - 2
                    ((4,5,6,7),self.color[1]),    #White   - 1
                    ((2,6,7,3),self.color[5]),    
                    ((0,1,2,3),self.color[0]),    
                    ((0,1,5,4),self.color[3]),    
                    ((1,2,6,5),self.color[4]))    

    if config == 'bo':
		  self.faces = (((0,3,7,4),self.color[2]),    #blue    - 2
                    ((4,5,6,7),self.color[3]),    #orange  - 3
                    ((2,6,7,3),self.color[1]),    
                    ((0,1,2,3),self.color[5]),    
                    ((0,1,5,4),self.color[0]),    
                    ((1,2,6,5),self.color[4]))   

    if config == 'by':
		  self.faces = (((0,3,7,4),self.color[2]),    #blue    - 2
                    ((4,5,6,7),self.color[0]),    #yellow  - 0
                    ((2,6,7,3),self.color[3]),    
                    ((0,1,2,3),self.color[1]),    
                    ((0,1,5,4),self.color[5]),    
                    ((1,2,6,5),self.color[4]))    

    if config == 'br':
		  self.faces = (((0,3,7,4),self.color[2]),    #blue    - 2
                    ((4,5,6,7),self.color[5]),    #red     - 5
                    ((2,6,7,3),self.color[0]),    
                    ((0,1,2,3),self.color[3]),    
                    ((0,1,5,4),self.color[1]),    
                    ((1,2,6,5),self.color[4]))    













