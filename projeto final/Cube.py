class Cube :
	def __init__(self, center, a):
		self.vertex = ((center[0]+a/2.0, center[1]+a/2.0, center[2]-a/2.0),
									 (center[0]+a/2.0, center[1]-a/2.0, center[2]-a/2.0),
									 (center[0]-a/2.0, center[1]-a/2.0, center[2]-a/2.0),
									 (center[0]-a/2.0, center[1]+a/2.0, center[2]-a/2.0),
									 (center[0]+a/2.0, center[1]+a/2.0, center[2]+a/2.0),
									 (center[0]+a/2.0, center[1]-a/2.0, center[2]+a/2.0),
									 (center[0]-a/2.0, center[1]-a/2.0, center[2]+a/2.0),
									 (center[0]-a/2.0, center[1]+a/2.0, center[2]+a/2.0))
		
		self.faces = ((0,1,2,3),
									(4,5,6,7),
									(0,1,5,4),
									(1,2,6,5),
									(2,6,7,3),
									(0,3,7,4))
		
