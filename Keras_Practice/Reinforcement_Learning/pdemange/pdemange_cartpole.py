from keras.layers import Dense
from keras.models import Sequential
from collections import deque
import random 
import numpy as np
import gym


class ReinforcementModel:
  def __init__(self, env):
    self.learningRate = .01
    self.gamma = .9
    self.epsilonRandom = 1
    self.epsilonDecay = .995
    self.epsilonMin = .01
    self.memory = deque(maxlen=2000)
    self.env = env
    self.network = self.buildModel()
    
  def buildModel(self):
    model = Sequential()
    environmentShape = self.env.observation_space.shape
    model.add(Dense(24, input_dim=environmentShape[0], activation='relu'))
    model.add(Dense(48, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(self.env.action_space.n))
    model.compile(loss='mse', optimizer='adam')
    model.optimizer.lr = self.learningRate
    return model
  
  def memAdd(self, state, action, reward, newState, done):
    self.memory.append([state, action, reward, newState, done])
  
  def act(self, state):
    self.epsilonRandom *= self.epsilonDecay
    self.epsilonRandom = max(self.epsilonMin, self.epsilonRandom)
    if np.random.random() < self.epsilonRandom:
      return self.env.action_space.sample()
    return np.argmax(self.model.predict(state)[0])
  
  def replay(self):
    batchSample = 32
    #If we don't have enough memory for it to learn, get some more!
    if len(self.memory) < batchSample:
      return 
    samples = random.sample(self.memory, batchSample)
    for sample in samples:
      state, action, reward, nextState, done = sample
      target = self.network.predict(state)
      if done: 
        target[0][action] = reward
      else:
        target[0][action] = reward + max(self.network.predict(nextState)[0]) * self.gamma
      self.network.fit(state, target, epochs=1, verbose=0)
    
if __name__ == '__main__':
  env = gym.make('CartPole-v0')
  trials = 100
  trialLength = 400
  step = []
  dqn = ReinforcementModel(env)
  for trial in range(trials):
    currState = env.reset().reshape(1,4)
    for step in range(trialLength):
      action = dqn.act(currState)
      env.render()
      newState, reward, done, _ = env.step(action)
      if done:
        reward = -10
      newState = newState.reshape(1,2)
      dqn.remember(currState, action, reward, newState, done)
      dqn.replay()
      currState = newState
      if done:
        break
    if step <= trialLength:
      print('Failed to complete trial!')
    else:
      print('Completed the trial!')
