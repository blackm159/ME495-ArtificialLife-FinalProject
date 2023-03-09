import pybullet as p

class WORLD:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world" + str(self.solutionID) + ".sdf")