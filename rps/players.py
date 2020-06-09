import numpy as np

class RPSStaticPlayer:
    def __init__(self, name, r_freq, p_freq, s_freq):
        self.name = name
        self.r = r_freq / (r_freq + p_freq + s_freq)
        self.p = p_freq / (r_freq + p_freq + s_freq)
        self.s = s_freq / (r_freq + p_freq + s_freq)
        self.dist = [self.r, self.p, self.s]
        self.wins = 0

    def action(self):
        return np.random.choice(["rock", "paper", "scissors"], p=self.dist)

    def win(self):
        self.wins += 1
        return self.name
