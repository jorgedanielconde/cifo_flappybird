from random import uniform, random, choice
from operator import attrgetter
import time



class Individual:
    ''' Holds a weight set that can be used for the neural network '''
    
    def __init__(self, representation = None, size = 5, valid_set = [0, 1], nnNumberOfInputs = 4):
        # TODO size and nnNumberofInputs refer to the same thing, figure this out!!
        self.representation = []
        self.valid_set = valid_set

        if representation is None:
            # generate random weights for layer zero (input size * number of neurons)
            for _ in range(nnNumberOfInputs):
                self.representation = self.representation + [round(uniform(valid_set[0], valid_set[1]), 4) for _ in range(size)]

            # generate random weights for layer one (number of neurons of layer 0)
            self.representation = self.representation + [round(uniform(valid_set[0], valid_set[1]), 4) for _ in range(size)]
            
        else:
            self.representation = representation

        self.fitness = self.calc_fitness(numberOfRepeats = 3) #set here the number of repeats for each bird, deafult is 1
    
    def update_fitness(self):
        ''' Recalculate fitness - to be used after mutation'''
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")
    
    def get_fitness(self):
        return self.fitness

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual: {self.representation}, Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    valid_set=kwargs["valid_set"],
                )
            )

    def evolve(self, gens, select, tournamentSize, crossover, mutate, crossoverProbab, mutationProbab, elitism):
        for gen in range(gens):
            
            startTime = time.time()
    
            newPop = []
            popSizeOdd = (self.size % 2 == 1)

            # select the best indiv in the pop and add it to newPop
            if elitism:
                elite = self.get_elite()
                if popSizeOdd:
                    # when popsize is odd simply add elitism is true simply add the elite member to the newPop
                    newPop.append(elite)
                else: 
                    # when popsize is even we need to add the elite member as well as another random member 
                    newPop.append(elite)
                    randomIndiv = choice(self.individuals)
                    newPop.append(randomIndiv)
            else: 
                if popSizeOdd: 
                    # when no elitism and popsize is odd: we need to add a random member to the newPop
                    randomIndiv = choice(self.individuals)
                    newPop.append(randomIndiv)

            while len(newPop) < self.size:
                # Selection
                parent1, parent2 = select(self, tournamentSize), select(self, tournamentSize)
                # Crossover
                offspring1, offspring2 = crossover(parent1, parent2, crossoverProbab)
                # Mutation
                offspring1 = mutate(offspring1, mutationProbab)
                offspring2 = mutate(offspring2, mutationProbab)

                newPop.append(offspring1)
                newPop.append(offspring2)

            self.individuals = newPop
            endTime = time.time()
            timeTook = endTime - startTime
            print(f'Gen {gen} took {round(timeTook)} seconds, Best fitness: {max(self.individuals, key=attrgetter("fitness")).fitness}')
    

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])}, first indiv: {self.individuals[0]} \n)"

    def get_elite(self):
        ''' Retrieve the individual with the best fitness'''
        elite = self.individuals[0]
        #print(elite.get_fitness())
        for ind in self.individuals[1:]:
            #print(ind.get_fitness(),elite.get_fitness()) #to be deleted: Test to see why sometimes get_elite doesn't work
            if ind.get_fitness() > elite.get_fitness():
                elite = ind
        #elite = max(self.individuals, key=attrgetter("fitness"))   #Alternative
        return elite
