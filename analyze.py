import numpy as np
import matplotlib.pyplot

#targetAngles = np.load('data/targetAngles.npy')
#matplotlib.pyplot.plot(targetAngles)

#backLegSensorValues = np.load('data/backLegSensorValues.npy')
#frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

#print(backLegSensorValues)

#matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=2)
#matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg', linewidth=1.25)

backLegMotorValues = np.load('data/backLegMotorValues.npy')
frontLegMotorValues = np.load('data/frontLegMotorValues.npy')

matplotlib.pyplot.plot(backLegMotorValues, label='Back Leg', linewidth=2)
matplotlib.pyplot.plot(frontLegMotorValues, label='Front Leg', linewidth=1.25)

matplotlib.pyplot.legend()

matplotlib.pyplot.show()