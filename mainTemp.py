from solution import SOLUTION
import os
import constants as c
import time

os.system("del brain*.nndf")
os.system("del body*.urdf")
os.system("del fitness*.txt")
os.system("del tmp*.txt")


mySol = SOLUTION(0)
mySol.Evaluate("GUI")
