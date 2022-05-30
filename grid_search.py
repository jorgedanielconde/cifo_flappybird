from charles import Population, Individual
from fitness import calc_fitness
from selection import fps, tournament
from crossover import single_point_co, cycle_co, pmx_co, arithmetic_co
from mutation import binary_mutation, swap_mutation, inversion_mutation

import itertools
import pandas as pd
import numpy as np

# Monkey Patching
Individual.calc_fitness = calc_fitness

# define population params
popSize = 25
problemType = 'max'
solSize = 6 #aka number of neurons in the hidden layer
validSet = [-1, 1]


#grid search
params = {
         'numberOfGenerations':[100],
         'selectionAlg':[tournament], #fps is another option, Berfin said tournament will probably perform better
         'tournamentSize':[10],
         'crossoverAlgo':[cycle_co, pmx_co, arithmetic_co],           #single_point_co has issues with elitism
         'mutationAlg':[binary_mutation, swap_mutation, inversion_mutation],
         'crossoverProbab':[0.8],
         'mutationProbab':[0.2],
         'elitism': [True]
         }


#df where to store all the evolve output
# -------------------------------
#  Columns: n-th of generation
#  Rows: fitnesses for each of the pop.evolve in the subsequent for loop 
# -------------------------------
df = pd.DataFrame(columns=np.arange(1,101,1).tolist()) 
print(df)

# this was a test
#def myfunc(**args):
#    print(args)
list_of_strings_models=[]

keys = list(params)
for values in itertools.product(*map(params.get, keys)):
    #myfunc(**dict(zip(keys, values)))

    # initialize population
    pop = Population(size = popSize, optim = problemType, sol_size = solSize, valid_set = validSet)
    print('Population created: ', pop)

    pop.evolve(*values) #*values unpacks the values of the list of parameters as arguments to the function, otherwise they would be 1 argument
    #evolvedBestSolution = pop.get_elite()

    #save the string values specifics of each grid search combination and append it to a list
    x=str(values)
    list_of_strings_models.append(x)
    
    #save the list of fitness from charles and append it to the df
    list_of_fitness = pop.all_fitness_score
    print(list_of_fitness)
    df = df.append(pd.Series(list_of_fitness, index=np.arange(1,101,1).tolist()), ignore_index=True)
#we save the list of parameters settings to a text file
with open('combination_specifics.txt', 'w+') as fh:
        fh.write(''.join(list_of_strings_models))
df
df.to_csv('df.csv')