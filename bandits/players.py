import numpy as np


class GreedyBandit:
    def __init__(self, k):
        self.rewards = list()
        self.arm_samplemeans = np.zeros(k)
        self.arm_samplecounts = np.zeros(k)
        
    def choose(self):
        return np.random.choice(np.flatnonzero(self.arm_samplemeans == self.arm_samplemeans.max())) 

    def add_reward(self, arm, reward):
        self.rewards.append(reward)
        self.arm_samplecounts[arm] += 1
        self.arm_samplemeans[arm] += 1 / self.arm_samplecounts[arm] * (reward - self.arm_samplemeans[arm])


class GreedyBandit2:
    '''
    Uses greedy action selection like above, but initializes sample means at a higher value. Optimism under uncertainty.
    '''
    def __init__(self, k):
        self.rewards = list()
        self.arm_samplemeans = np.ones(k) * 10
        self.arm_samplecounts = np.zeros(k)
        
    def choose(self):
        return np.random.choice(np.flatnonzero(self.arm_samplemeans == self.arm_samplemeans.max())) 

    def add_reward(self, arm, reward):
        self.rewards.append(reward)
        self.arm_samplecounts[arm] += 1
        self.arm_samplemeans[arm] += 1 / self.arm_samplecounts[arm] * (reward - self.arm_samplemeans[arm])
