import numpy as np
import random

simLength = 1000

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

amplitude = np.pi/4.0
frequency = 10
phaseOffset = np.pi/8.0

backLegAmplitude = np.pi/4.0
backLegFrequency = 10
backLegPhaseOffset = np.pi/8.0

frontLegAmplitude = np.pi/4.0
frontLegFrequency = 10
frontLegPhaseOffset = 0

frontLegMotorValues = frontLegAmplitude * np.sin(frontLegFrequency * 
    np.linspace(0, 2*np.pi, 1000) + frontLegPhaseOffset)
backLegMotorValues = backLegAmplitude * np.sin(backLegFrequency * 
    np.linspace(0, 2*np.pi, 1000) + backLegPhaseOffset)

numberOfGenerations = 500
populationSize = 10

seed = 4#random.randint(0,100)

random.seed(seed)

numLinks = random.randint(1,5)

# arr2 = [[0 for col in range(5)] for row in range(10)]
# numSubLinks = [[0 for col in range(2)] for row in range(numLinks)]
totalNumLinks = 0#numLinks
numSubLinks = np.zeros(shape=(numLinks,2), dtype="object")
locTorso = []
for row in range(1,numLinks+1):
    locTorso.append(totalNumLinks)
    totalNumLinks = totalNumLinks + 1
    for col in range(1,2+1):
        numSubLinks[row-1,col-1] = random.randint(0,4)
        totalNumLinks = totalNumLinks + numSubLinks[row-1,col-1]

# print(numSubLinks)
# print(totalNumLinks)
# print(locTorso)

numSensorNeurons = random.randint(1,totalNumLinks)
numMotorNeurons = totalNumLinks - 1

motorJointRange = 0.3 #this does something with angle values