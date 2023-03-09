import numpy as np
import pyrosim.pyrosim as pyrosim

import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.values = np.zeros(c.simLength)
        
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if i == c.simLength - 1:
        #     print(self.values)

    def Save_Values(self):
        filename = 'data/' + self.linkName + 'SensorValues.npy'
        np.save(filename, self.values)