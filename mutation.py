from random import randint, uniform, sample

def binary_mutation(individual, mutationProbab):
    """Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    # decide whether to perform mutation
    if mutationProbab > uniform(0, 1):
        # select the index of the weight to be mutated
        mutationPoint = randint(0, len(individual) - 1)
        # generate random new weight 
        individual[mutationPoint] = round(uniform(individual.valid_set[0], individual.valid_set[1]), 4)
        # update fitness of indiv after mutation
        individual.update_fitness()
    return individual

def swap_mutation(individual, mutationProbab):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    if mutationProbab > uniform(0, 1):
        mut_points = sample(range(len(individual)), 2)
        # Swap them
        individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]
        # update fitness of indiv after mutation
        individual.update_fitness()

    return individual

def inversion_mutation(individual, mutationProbab):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    if mutationProbab > uniform(0, 1):
        # Position of the start and end of substring
        mut_points = sample(range(len(individual)), 2)
        # This method assumes that the second point is after (on the right of) the first one
        # Sort the list
        mut_points.sort()
        # Invert for the mutation
        individual[mut_points[0]:mut_points[1]] = individual[mut_points[0]:mut_points[1]][::-1]

    return individual