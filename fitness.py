import flappy_bird as fp
import pygame
import os
#import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

WIN_WIDTH = 600
WIN_HEIGHT = 800
PIPE_VEL = 3
FLOOR = 730
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())


""" def build_neural_network(weightList, numberOfGameParams=5):
    # 
    numberOfNeurons = int(len(weightList) / (numberOfGameParams + 1))
    #print('len weight list: ', len(weightList))
    #print('game params: ', numberOfGameParams)
    model = Sequential()
    model.add(Dense(units = numberOfNeurons, activation = 'relu', input_shape = (numberOfGameParams,)))
    
    # TODO decide on activation function

    model.add(Dense(units = 1, activation = 'sigmoid'))
    #model.add(Dense(units = 1, activation = 'linear'))
    model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    #print('nn weights after init', model.layers[0].get_weights()[0])
    # set the weights according to the individual's representation

    # split the weight list: weights for layer 0 and weights for layer 1
    splitPoint = numberOfGameParams * numberOfNeurons
    weightsLayerZero = np.array(weightList[:splitPoint]).reshape((numberOfGameParams, numberOfNeurons))
    weightsLayerOne = np.array(weightList[splitPoint:]).reshape((numberOfNeurons, 1))

    # generate bias lists
    #biasLayerZero = [np.ones((numberOfGameParams, numberOfNeurons))]
    biasLayerZero = np.ones((numberOfNeurons))
    biasLayerOne = np.ones((1))

    #print('weights to set :', weightsLayerZero)

    # set weights of model according to the representation of the individual
    model.layers[0].set_weights([weightsLayerZero, biasLayerZero])
    #model.layers[0].set_weights(weightsLayerZero)


    #print('nn weights layer 2 after init', model.layers[1].get_weights()[0])
    #print('weights to set layer 2:', weightsLayerOne)
    model.layers[1].set_weights([weightsLayerOne, biasLayerOne])

    return model
 """

class neural_network(object):
  def __init__(self,weightList):
    #parameters
    self.inputSize = 3
    self.outputSize = 1
    self.hiddenSize = 6

    #weights
    self.W1 = np.array(weightList[:self.inputSize*self.hiddenSize]).reshape(self.inputSize, self.hiddenSize) # (3x6) weight matrix from input to hidden layer
    self.W2 = np.array(weightList[self.inputSize*self.hiddenSize:]).reshape(self.hiddenSize,self.outputSize) # (6x1) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))


def play_flappy_bird(nn):
    return fp.main(WIN, nn)


def calc_fitness(self, numberOfRepeats = 1):
    avgScore = 0
    weightList = self.representation
    #print('indiv weight list: ', weightList)
    nn = neural_network(weightList)
    for _ in range(numberOfRepeats): 
        currentScore = 0
        #print('nn weights', nn.layers[0].get_weights()[0])
        currentScore = play_flappy_bird(nn)
        avgScore += currentScore

    # for test purposes 1 - to be deleted once the fitness can be calculated by playing the game
    #dummyFitness = sum(self.representation)

    # for test purposes 2 - to be deleted once the fitness can be calculated by playing the game
    #dummyFitness = sum(self.representation[:3]) - sum(self.representation[3:])
 
    #return dummyFitness
    return avgScore / numberOfRepeats

    