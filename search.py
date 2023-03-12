import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(5):
#     os.system("py generate.py")
#     os.system("py simulate.py")

# os.system("del brain*.nndf")
# os.system("del body*.urdf")
# os.system("del fitness*.txt")
# os.system("del tmp*.txt")
# os.system("del world*.sdf")


# COEVOLUTION
os.system("py removeFiles.py")

phc_coevolve = PARALLEL_HILL_CLIMBER("CoEvolution")

phc_coevolve.Evolve()

input("Please press enter when ready to record best \n")

phc_coevolve.Show_Best()

# # input("Please press enter to continue to brain first evolution \n")

# # ***********************************************************************
# # BRAIN FIRST HALF
# os.system("py removeFiles.py")

# phc_brain = PARALLEL_HILL_CLIMBER("BrainBody")

# phc_brain.Evolve()

# input("Please press enter when ready to record best \n")

# phc_brain.Show_Best()

# input("Please press enter to continue to body first evolution \n")

# # ***********************************************************************
# # BODY FIRT HALF
# os.system("py removeFiles.py")

# phc_body = PARALLEL_HILL_CLIMBER("BodyBrain")

# phc_body.Evolve()

# input("Please press enter when ready to record best \n")

# phc_body.Show_Best()

# input("Please press enter to continue to probability evolution \n")

# # ***********************************************************************
# # PROBABILITY
# os.system("py removeFiles.py")

# phc_prob = PARALLEL_HILL_CLIMBER("Probability")

# phc_prob.Evolve()

# input("Please press enter when ready to record best \n")

# phc_prob.Show_Best()



# os.system("py removeFiles.py")

# os.system("del brain*.nndf")
# os.system("del body*.urdf")
# os.system("del fitness*.txt")
# os.system("del tmp*.txt")
# os.system("del world*.sdf")

