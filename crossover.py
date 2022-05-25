from random import randint, random, uniform, sample
from charles import Individual

def single_point_co(p1, p2, crossoverProbab):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    #print(p1)
    #print(p2)
    # decide whether to perform crossover
    if crossoverProbab > uniform(0, 1):
        # select the index where to cut the dna s 
        co_point = randint(1, len(p1)-2)
        #print('copoint:', co_point)
        newRepr1 = p1.representation[:co_point] + p2.representation[co_point:]
        #print('newRepr1:', newRepr1)
        offspring1 = Individual(representation = newRepr1, size=len(p1), valid_set=p1.valid_set)
        newRepr2 = p2.representation[:co_point] + p1.representation[co_point:]
        #print('newRepr2:', newRepr2)
        offspring2 = Individual(representation = newRepr2, size=len(p1), valid_set=p1.valid_set)
        #print('o1', offspring1)
        #print('o2', offspring2)
    else: 
        offspring1, offspring2 = p1, p2

    return offspring1, offspring2

def cycle_co(p1, p2, crossoverProbab):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # Offspring placeholders - None values make it easy to debug for errors
    if crossoverProbab > uniform(0, 1):
        offspring1 = [None] * len(p1)
        offspring2 = [None] * len(p2)
        # While there are still None values in offspring, get the first index of
        # None and start a "cycle" according to the cycle crossover method
        while None in offspring1:
            index = offspring1.index(None)

            #with a random probability we change the values for the parents (reminder!)
            if random() > uniform(0, 1):
                offspring1[index] = p1[index]
                offspring2[index] = p2[index]
            else:
                offspring1[index] = p2[index]
                offspring2[index] = p1[index]

                          
    else: 
        offspring1, offspring2 = p1, p2

    o1 = Individual(representation = offspring1, size=len(p1), valid_set=p1.valid_set)
    o2 = Individual(representation = offspring2, size=len(p1), valid_set=p1.valid_set)

    return o1, o2

def pmx_co(p1, p2, crossoverProbab):
    """Implementation of partially matched/mapped crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    if crossoverProbab > uniform(0, 1):
        co_points = sample(range(len(p1)), 4)
        co_points.sort()

        #we switch values corresponding in the two co_points
        def PMX(x, y):
            o = [None] * len(x)

            o[co_points[0]:co_points[1]] = x[co_points[0]:co_points[1]]
            o[co_points[2]:co_points[3]] = x[co_points[2]:co_points[3]]

            while None in o:
                index = o.index(None)
                o[index] = y[index]
            return o

        o1, o2 = PMX(p1, p2), PMX(p2, p1)
    else: 
        o1, o2 = p1, p2
    
    offspring1 = Individual(representation = o1, size=len(p1), valid_set=p1.valid_set)
    offspring2 = Individual(representation = o2, size=len(p1), valid_set=p1.valid_set)

    return offspring1, offspring2

def arithmetic_co(p1, p2, crossoverProbab):
    """Implementation of arithmetic crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    if crossoverProbab > uniform(0, 1):
    # Offspring placeholders - None values make it easy to debug for errors
        offspring1 = [None] * len(p1)
        offspring2 = [None] * len(p1)
        # Set a value for alpha between 0 and 1
        alpha = uniform(0, 1)
        # Take weighted sum of two parents, invert alpha for second offspring
        for i in range(len(p1)):
            offspring1[i] = p1[i] * alpha + (1 - alpha) * p2[i]
            offspring2[i] = p2[i] * alpha + (1 - alpha) * p1[i]
        
    else: 
        offspring1, offspring2 = p1, p2

    o1 = Individual(representation = offspring1, size=len(p1), valid_set=p1.valid_set)
    o2 = Individual(representation = offspring2, size=len(p1), valid_set=p1.valid_set)

    return o1, o2