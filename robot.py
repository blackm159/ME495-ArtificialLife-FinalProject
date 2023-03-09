import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import stat

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID):
        self.myID = solutionID
        self.robotId = p.loadURDF("body" + str(self.myID) +".urdf")
        self.nn = NEURAL_NETWORK("brain" + str(self.myID) +".nndf")

        os.system("del brain" + str(self.myID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self, i):
        for linkName in self.sensors:
           self.sensors[linkName].Get_Value(i)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        # print("self.motors = ", self.motors)

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                
                self.motors[jointName.encode()].Set_Value(desiredAngle, self.robotId)

                #print("#" + neuronName + " " + jointName + " = " + str(desiredAngle))

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        # stateOfLinkZero = p.getLinkState(self.robotId, 0)
        # positionOfLinkZero = stateOfLinkZero[0]
        # xCoordinateOfLinkZero = positionOfLinkZero[0]

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        filename = str(self.myID) +".txt"
        f = open("tmp" + filename, "w")
        f.write(str(xPosition))
        f.close()
        os.chmod("tmp" + filename, stat.S_IRWXU)
        os.system("rename tmp" + filename + " fitness" + filename)

        

        