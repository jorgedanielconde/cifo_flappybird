from charles import Population, Individual
from fitness import calc_fitness
from selection import fps, tournament
from crossover import single_point_co #cycle_co, pmx_co
from mutation import binary_mutation #,swap_mutation, inversion_mutation

import itertools
import pandas as pd
import numpy as np

# Monkey Patching
Individual.calc_fitness = calc_fitness

# define population params
popSize = 50
problemType = 'max'
solSize = 6 #aka number of neurons in the hidden layer
validSet = [-1, 1]

# initialize population
pop = Population(size = popSize, optim = problemType, sol_size = solSize, valid_set = validSet)

print('Population created: ', pop)

'''
# define evolution params
numberOfGenerations = 100
selectionAlg = fps
tournamentSize = None  # set to None if selectionAlg is not tournament
crossoverAlg = single_point_co
crossoverProbab = 0.8
mutationAlg = binary_mutation
mutationProbab = 0.3
elitism = True

# do evolution

pop.evolve(gens = numberOfGenerations,
           select = selectionAlg,
           tournamentSize = tournamentSize, # set to None if selectionAlg is not tournament
           crossover = crossoverAlg,
           mutate = mutationAlg,
           crossoverProbab = crossoverProbab,
           mutationProbab = mutationProbab,
           elitism = elitism)

evolvedBestSolution = pop.get_elite()
'''

#grid search
params = {
         'numberOfGenerations':[100, 200],
         'selectionAlg':[tournament,fps],
         'tournamentSize':[4, 15, 40],
         'crossoverAlgo':[single_point_co,'cycle_co','pmx_co'],
         'mutationAlg':[binary_mutation, 'swap_mutation', 'inversion_mutation'],
         'crossoverProbab':[0.5, 0.8],
         'mutationProbab':[0.3, 0.6],
         'elitism': [True]
         }



#df where to store all the evolve output
# -------------------------------
#  Columns: n-th of generation
#  Rows: fitnesses for each of the pop.evolve in the subsequent for loop 
# -------------------------------
df = pd.DataFrame(columns=np.arange(0,100,1).tolist()) 
print(df)

# this was a test
#def myfunc(**args):
#    print(args)

keys = list(params)
for values in itertools.product(*map(params.get, keys)):
    #myfunc(**dict(zip(keys, values)))
    pop.evolve(*values) #*values unpacks the values of the list of parameters as arguments to the function, otherwise they would be 1 argument
    evolvedBestSolution = pop.get_elite()

    ##append list of fitness (that has to be created in charles.py) to the df 
