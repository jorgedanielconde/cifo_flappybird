from charles import Population, Individual
from fitness import calc_fitness
from selection import fps, tournament
from crossover import single_point_co, cycle_co, pmx_co, arithmetic_co
from mutation import binary_mutation, swap_mutation, inversion_mutation

# Monkey Patching
Individual.calc_fitness = calc_fitness

# define population params
popSize = 50
problemType = 'max'
solSize = 6
validSet = [-1, 1]

# initialize population
pop = Population(size = popSize, optim = problemType, sol_size = solSize, valid_set = validSet)

print('Population created: ', pop)

# define evolution params
numberOfGenerations = 100
selectionAlg = tournament
tournamentSize = 10  # set to None if selectionAlg is not tournament
crossoverAlg = arithmetic_co
crossoverProbab = 0.8
mutationAlg = inversion_mutation
mutationProbab = 0.3
elitism = True

# do evolution
pop.evolve(gens = numberOfGenerations, select = selectionAlg, tournamentSize = tournamentSize, crossover = crossoverAlg,
            mutate = mutationAlg, crossoverProbab = crossoverProbab, mutationProbab = mutationProbab, elitism = elitism)

evolvedBestSolution = pop.get_elite()