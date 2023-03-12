import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import stat


class SOLUTION:
    def __init__(self, nextAvailableID, evolveType):
        self.myID = nextAvailableID
        self.evolveType = evolveType
        # self.generationCounter = 0
        self.seed = c.seed
        random.seed(self.seed)

        self.numLinks = c.numLinks
        self.numSubLinks = c.numSubLinks

        self.numSensorNeurons = c.numSensorNeurons

        self.startZ = 3

        self.linkNames = []
        self.jointNames = []
        self.x = {}
        self.y = {}
        self.z = {}
        self.myColor = {}
        self.jointAxis = {}
        self.dir = {}
        self.subJointPos = {}
        self.subJointParent = {}
        self.subJointChild = {}
        self.linkPos = {}

        self.randSensors = random.sample(range(0,c.totalNumLinks), c.numSensorNeurons)
        self.randSensors.sort()

        for ind in range(0,self.numLinks):
            self.linkNames.append("Body"+str(ind+1)+"."+str(0)+"."+str(0))
            self.x[self.linkNames[ind]] = random.uniform(1.0,1.25)
            self.y[self.linkNames[ind]] = random.uniform(0.5,1.25)
            self.z[self.linkNames[ind]] = random.uniform(0.5,1.25)
            if ind in self.randSensors:
                self.myColor[self.linkNames[ind]] = "green"
            else:
                self.myColor[self.linkNames[ind]] = "blue"

            if ind > 0:
                self.jointNames.append("Body"+str(ind)+"."+str(0)+"."+str(0)+"_Body"+str(ind+1)+"."+str(0)+"."+str(0))
                jointDir = random.randint(1,3)
                # 1 is x axis
                # 2 is y axis
                # 3 is z axis
                if jointDir == 1:
                    self.jointAxis[self.jointNames[ind-1]] = "1 0 0"
                elif jointDir == 2:
                    self.jointAxis[self.jointNames[ind-1]] = "0 1 0"
                elif jointDir == 3:
                    self.jointAxis[self.jointNames[ind-1]] = "0 0 1"
            
                    
        for row in range(1, self.numLinks+1):
            for col in range(1,2+1):
                for num in range(0, self.numSubLinks[row-1,col-1]):
                    self.linkNames.append("Body"+str(row)+"."+str(col)+"."+str(num))

                    ind = ind + 1
                    self.x[self.linkNames[ind]] = random.uniform(0.25,0.75)
                    self.y[self.linkNames[ind]] = random.uniform(0.25,0.75)
                    self.z[self.linkNames[ind]] = random.uniform(0.5,0.75)
                    if ind in self.randSensors:
                        self.myColor[self.linkNames[ind]] = "green"
                    else:
                        self.myColor[self.linkNames[ind]] = "blue"

                    if col == 1: # negative side joint
                        negMultY = -1
                    else:
                        negMultY = 1

                    if num == 0:
                        # joint name to torso
                        self.jointNames.append("Body"+str(row)+"."+str(0)+"."+str(0)+"_Body"+str(row)+"."+str(col)+"."+str(num))
                        jointDir = random.randint(1,3)
                        # 1 is x axis
                        # 2 is y axis
                        # 3 is z axis
                        if jointDir == 1:
                            self.jointAxis[self.jointNames[ind-1]] = "1 0 0"
                        elif jointDir == 2:
                            self.jointAxis[self.jointNames[ind-1]] = "0 1 0"
                        elif jointDir == 3:
                            self.jointAxis[self.jointNames[ind-1]] = "0 0 1"
                        
                        self.dir[self.jointNames[ind-1]] = 2
                        # 1 is down in -z direction
                        # 2 is left/right in +/-y direction

                        self.linkPos[self.linkNames[ind]] = [0, negMultY*self.y[self.linkNames[ind]]/2,0]

                        if row == 1:
                            # absolute position
                            self.subJointPos[self.jointNames[ind-1]] = [0, negMultY*self.y["Body"+str(row)+"."+str(0)+"."+str(0)]/2, self.startZ]
                            self.subJointParent[self.jointNames[ind-1]] = "Body"+str(row)+"."+str(0)+"."+str(0)
                            self.subJointChild[self.jointNames[ind-1]] = self.linkNames[ind]
                        else:
                            # relative position
                            self.subJointPos[self.jointNames[ind-1]] = [self.x["Body"+str(row)+"."+str(0)+"."+str(0)]/2, 
                                                                        negMultY*self.y["Body"+str(row)+"."+str(0)+"."+str(0)]/2, 0]
                            self.subJointParent[self.jointNames[ind-1]] = "Body"+str(row)+"."+str(0)+"."+str(0)
                            self.subJointChild[self.jointNames[ind-1]] = self.linkNames[ind]


                    elif num > 0:
                        # joint to previous num
                        self.jointNames.append("Body"+str(row)+"."+str(col)+"."+str(num-1)+"_Body"+str(row)+"."+str(col)+"."+str(num))
                        jointDir = random.randint(1,3)
                        # 1 is x axis
                        # 2 is y axis
                        # 3 is z axis
                        if jointDir == 1:
                            self.jointAxis[self.jointNames[ind-1]] = "1 0 0"
                        elif jointDir == 2:
                            self.jointAxis[self.jointNames[ind-1]] = "0 1 0"
                        elif jointDir == 3:
                            self.jointAxis[self.jointNames[ind-1]] = "0 0 1"
                        
                        self.dir[self.jointNames[ind-1]] = random.randint(1,2)
                        # 1 is down in -z direction
                        # 2 is left/right in +/-y direction
                        
                        self.subJointParent[self.jointNames[ind-1]] = self.linkNames[ind-1]
                        self.subJointChild[self.jointNames[ind-1]] = self.linkNames[ind]

                        if prevDir == 2 and self.dir[self.jointNames[ind-1]] == 2:
                            self.subJointPos[self.jointNames[ind-1]] = [0, negMultY*self.y[self.linkNames[ind-1]], 0]
                            self.linkPos[self.linkNames[ind]] = [0, negMultY*self.y[self.linkNames[ind]]/2,0]

                        elif prevDir == 1 and self.dir[self.jointNames[ind-1]] == 1:
                            self.subJointPos[self.jointNames[ind-1]] = [0, 0, -1*self.z[self.linkNames[ind-1]]]
                            self.linkPos[self.linkNames[ind]] = [0, 0, -1*self.z[self.linkNames[ind]]/2]

                        elif prevDir == 2 and self.dir[self.jointNames[ind-1]] == 1:
                            self.subJointPos[self.jointNames[ind-1]] = [0, negMultY*self.y[self.linkNames[ind-1]]/2,
                                                                         -1*self.z[self.linkNames[ind-1]]/2]
                            self.linkPos[self.linkNames[ind]] = [0, 0, -1*self.z[self.linkNames[ind]]/2]

                        elif prevDir == 1 and self.dir[self.jointNames[ind-1]] == 2:
                            self.subJointPos[self.jointNames[ind-1]] = [0, negMultY*self.y[self.linkNames[ind-1]]/2,
                                                                         -1*self.z[self.linkNames[ind-1]]/2]
                            self.linkPos[self.linkNames[ind]] = [0, negMultY*self.y[self.linkNames[ind]]/2, 0]


                    prevDir = self.dir[self.jointNames[ind-1]]


        # print(self.linkNames)
        # print(self.jointNames)


        # a = 3
        # b = 2
        self.weights = np.empty(shape=(self.numSensorNeurons,c.numMotorNeurons), dtype='object')
        # self.weights = np.empty(shape=(a,b), dtype='object')
        for row in range(0, self.numSensorNeurons):
            for col in range(0, c.numMotorNeurons):
                self.weights[row,col] = np.random.rand()
        self.weights = self.weights * 2 - 1


    def Evaluate(self, directOrGUI):
        # pass
        self.Create_Body()
        self.Create_Brain()

        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))

        # fitnessFileName = "fitness" + str(self.myID) + ".txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        # fitnessFile = open(fitnessFileName, "r")
        # self.fitness = float(fitnessFile.read())
        # print("self.fitness = " + str(self.fitness))
        # fitnessFile.close()

    def Start_Simulation(self, directOrGUI):
        
        self.Create_Body()
        self.Create_Brain()

        #print("start /B py simulate.py " + directOrGUI + " " + str(self.myID))
        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))
        

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.2)

        try:
            fitnessFile = open(fitnessFileName, "r")
        except:
            os.chmod(fitnessFileName, stat.S_IRWXU)
            fitnessFile = open(fitnessFileName, "r")

        self.fitness = float(fitnessFile.read())
        # print("\nself.fitness = " + str(self.fitness))
        fitnessFile.close()
        os.system("del " + fitnessFileName)

    def Mutate(self, generationCounter):
        
        brainFlag = 0
        sensorFlag = 0 # part of brain evolution
        bodyFlag = 0

        if self.evolveType == "CoEvolution":
            brainFlag = 1
            sensorFlag = 1
            bodyFlag = 1

        elif self.evolveType == "BodyBrain":
            if generationCounter < c.numberOfGenerations/2:
                bodyFlag = 1
            else:
                brainFlag = 1
                sensorFlag = 1

        elif self.evolveType == "BrainBody":
            if generationCounter < c.numberOfGenerations/2:
                brainFlag = 1
                sensorFlag = 1
            else:
                bodyFlag = 1

        elif self.evolveType == "Probability":
            a = random.randint(0,2)

            if a == 0:
                brainFlag = 1
            elif a == 1:
                sensorFlag = 1
            elif a == 2:
                bodyFlag = 1
            else:
                print("No evolution for " + str(generationCounter) + " with ID " + str(self.myID))

        else:
            print("Invalid evolution type")


        if brainFlag == 1:
            print("Evolving brain for " + str(generationCounter))

            if self.numSensorNeurons > 1:
                randRow = random.randint(0,self.numSensorNeurons-1)
            else:
                randRow = 0
            randCol = random.randint(0,c.numMotorNeurons-1)

            self.weights[randRow, randCol] = random.random()*2 - 1

        if sensorFlag == 1:
            print("Evolving sensors for " + str(generationCounter))

            randSensor = random.randint(0,len(self.linkNames)-1)
            if randSensor in self.randSensors and self.numSensorNeurons > 1:
                self.myColor[self.linkNames[randSensor]] = "blue"
                ind = self.randSensors.index(randSensor)
                self.randSensors.remove(randSensor)
                self.weights = np.delete(self.weights, ind, 0)
                self.numSensorNeurons = self.numSensorNeurons - 1
            else:
                self.myColor[self.linkNames[randSensor]] = "green"
                self.randSensors.append(randSensor)
                # self.randSensors.sort()
                self.numSensorNeurons = self.numSensorNeurons + 1
                newrow = []
                for col in range(0, c.numMotorNeurons):
                    newrow.append(np.random.rand()*2 - 1)
                self.weights = np.append(self.weights, [newrow], axis=0)


        if bodyFlag == 1:
            print("Evolving body for " + str(generationCounter))

            randJointAxis = random.randint(0,len(self.jointNames)-1)
            jointDir = random.randint(1,3)
            if jointDir == 1:
                self.jointAxis[self.jointNames[randJointAxis]] = "1 0 0"
            elif jointDir == 2:
                self.jointAxis[self.jointNames[randJointAxis]] = "0 1 0"
            elif jointDir == 3:
                self.jointAxis[self.jointNames[randJointAxis]] = "0 0 1"



        # self.generationCounter = self.generationCounter + 1


        # # self.weights = np.empty(shape=(a,b), dtype='object')
        # for col in range(0, c.numMotorNeurons):
        #     self.weights[self.numSensorNeurons,col] = np.random.rand()*2 - 1


        # randLink = random.randint(0,len(self.linkNames)-1)
        # if randLink <= self.numLinks:
        #     self.x[self.linkNames[randLink]] = random.uniform(1.0,1.25)
        #     self.y[self.linkNames[randLink]] = random.uniform(0.5,1.25)
        #     self.z[self.linkNames[randLink]] = random.uniform(0.5,1.25)
        # else:
        #     self.x[self.linkNames[randLink]] = random.uniform(0.25,0.75)
        #     self.y[self.linkNames[randLink]] = random.uniform(0.25,0.75)
        #     self.z[self.linkNames[randLink]] = random.uniform(0.5,0.75)


    def Set_ID(self, newID):
        self.myID = newID

    def Create_World(self):
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        # length = 1
        # width = 1
        # height = 1
        # x = -2
        # y = -2
        # z = height/2

        # pyrosim.Send_Cube(name="Box", pos = [-2,-2,height/2], size = [length,width,height])

        pyrosim.End()

    def Create_Body(self):
        self.Create_World()

        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        

        # for ind in range(0, len(self.linkNames)):
        for indLink in range(0, self.numLinks):
            bodyName = self.linkNames[indLink]
            if indLink == 0:
                # absolute coordinates
                pyrosim.Send_Cube(name=bodyName, pos = [0, 0, self.startZ], 
                                  size = [self.x[bodyName], self.y[bodyName], self.z[bodyName]], 
                                  materialColor=self.myColor[bodyName])
            else:
                # relative coordinates
                pyrosim.Send_Cube(name=bodyName, pos = [self.x[bodyName]/2, 0, 0], 
                                  size = [self.x[bodyName], self.y[bodyName], self.z[bodyName]], 
                                  materialColor=self.myColor[bodyName])
                
        for indLink in range(self.numLinks, len(self.linkNames)):
            bodyName = self.linkNames[indLink]
            pyrosim.Send_Cube(name=bodyName, pos = self.linkPos[bodyName], 
                                size = [self.x[bodyName], self.y[bodyName], self.z[bodyName]], 
                                materialColor=self.myColor[bodyName])
                
        for indJoint in range(0, self.numLinks-1):
            jointName = self.jointNames[indJoint]
            if indJoint == 0:
                # absolute coordinates
                pyrosim.Send_Joint( name = jointName, parent= self.linkNames[indJoint], 
                                   child = self.linkNames[indJoint+1],
                                   type = "revolute", 
                                   position = [self.x[self.linkNames[indJoint]]/2, 0, self.startZ], 
                                   jointAxis=self.jointAxis[jointName])

            else:
                # relative coordinates
                pyrosim.Send_Joint( name = jointName, parent= self.linkNames[indJoint], 
                                   child = self.linkNames[indJoint+1], 
                                   type = "revolute", 
                                   position = [self.x[self.linkNames[indJoint]], 0, 0], 
                                   jointAxis=self.jointAxis[jointName])
                
        for indJoint in range(self.numLinks-1, len(self.linkNames)-1):
            jointName = self.jointNames[indJoint]    
            pyrosim.Send_Joint( name = jointName, parent= self.subJointParent[jointName], 
                                child = self.subJointChild[jointName], 
                                type = "revolute", 
                                position = self.subJointPos[jointName], 
                                jointAxis=self.jointAxis[jointName])

       
        # print(self.linkNames)
        # print(self.jointNames)
        # print(self.x)
        # print(self.y)
        # print(self.z)

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # for joint in joint names create motor
        # have a counter variable for name ID
        # do sensors first

        # print(self.randSensors)

        counterNeuron = 0
        for ind in self.randSensors:
            pyrosim.Send_Sensor_Neuron(name = counterNeuron , linkName = self.linkNames[ind])
            counterNeuron = counterNeuron + 1

        for ind in range(0, c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron(name = counterNeuron , jointName = self.jointNames[ind])
            counterNeuron = counterNeuron + 1
        

        for currentRow in range(0, self.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                # print("i = " + str(i) + ", j = " + str(j))
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+self.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()