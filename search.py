import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(5):
#     os.system("py generate.py")
#     os.system("py simulate.py")

os.system("del brain*.nndf")
os.system("del body*.urdf")
os.system("del fitness*.txt")
os.system("del tmp*.txt")
os.system("del world*.sdf")

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

input("Please press enter when ready to record best \n")

phc.Show_Best()

# os.system("del brain*.nndf")
# os.system("del body*.urdf")
# os.system("del fitness*.txt")
# os.system("del tmp*.txt")
# os.system("del world*.sdf")

