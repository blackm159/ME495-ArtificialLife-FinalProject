import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np

from world import WORLD
from robot import ROBOT
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):

        if (directOrGUI == "GUI"):
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
            self.timeSleep = 0.005 #0.0075
        else: 
            self.physicsClient = p.connect(p.DIRECT)
            self.timeSleep = 0.00

        # self.physicsClient = p.connect(p.GUI)
        # self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD(solutionID)
        self.robot = ROBOT(solutionID)

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def run(self):
        for i in range(c.simLength):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            # print('i = ', i)
            # time.sleep(0.0075)
            time.sleep(self.timeSleep)

        # for linkName in self.robot.sensors:
        #     self.robot.sensors[linkName].Save_Values()
        # for jointName in self.robot.motors:
        #     self.robot.motors[jointName].Save_Values()
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()
    
    def __del__(self):
        p.disconnect()
    