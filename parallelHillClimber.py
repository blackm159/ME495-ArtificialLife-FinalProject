from solution import SOLUTION
import constants as c
import copy
import os
import random
import time

class PARALLEL_HILL_CLIMBER:
    def __init__(self, evolveType):
        # os.system("del brain*.nndf")
        # os.system("del body*.urdf")
        # os.system("del fitness*.txt")
        # os.system("del tmp*.txt")
        # self.parent = SOLUTION()

        self.evolveType = evolveType
        self.generationCounter = 1

        self.nextAvailableID = 0
        self.parents = {}
        for parent in range(0, c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID, self.evolveType)
            self.nextAvailableID = self.nextAvailableID + 1

        self.bestFitness = []

        self.seed = c.seed
        random.seed(self.seed)
        
    def Evolve(self):
        self.Evaluate(self.parents)

        tempBest = self.parents[0].fitness
        for key in self.parents:
            if self.parents[key].fitness < tempBest:
                # tempBestKey = key
                tempBest = self.parents[key].fitness
        
        self.bestFitness.append(tempBest)

        self.Show_Best()
        time.sleep(10)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        print(self.bestFitness)
        filename = self.evolveType + "_seed" + str(self.seed) +".txt"
        f = open(filename, "w")
        f.write(str(self.bestFitness))
        f.close()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate(self.generationCounter)

        self.generationCounter = self.generationCounter + 1

    def Select(self):
        for key in self.parents:
            if (self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]

        tempBest = self.parents[0].fitness
        for key in self.parents:
            if self.parents[key].fitness < tempBest:
                # tempBestKey = key
                tempBest = self.parents[key].fitness
        
        self.bestFitness.append(tempBest)

    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Print(self):
        print("\n")
        for key in self.parents:
            myStr = "\nParent Fitness: " + "{:.2f}".format(self.parents[key].fitness) + "\tChild Fitness: " + "{:.2f}".format(self.children[key].fitness)
            print(myStr)
        print("\n")

    def Show_Best(self):
        bestFit = self.parents[0].fitness
        bestKey = 0
        for key in self.parents:
            if self.parents[key].fitness < bestFit:
                bestKey = key
                bestFit = self.parents[key].fitness
        print("Best key " + str(bestKey))
        print("Best fit " + str(bestFit))
        self.parents[bestKey].Start_Simulation("GUI")


    # def __del__(self):
    #     os.system("del brain*.nndf")
    #     os.system("del body*.urdf")
    #     os.system("del fitness*.txt")
    #     os.system("del tmp*.txt")
    #     os.system("del world*.sdf")
