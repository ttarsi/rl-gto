import numpy as np


class Arm:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def sample(self):
        return np.random.normal(self.mean, self.std)


class kBandits:
    def __init__(self, k):
        self.arms = [Arm(np.random.normal(5,3), np.random.uniform(0.1, 10)) for _ in range(k)]

    def pull(self, arm):
        return self.arms[arm].sample()


if __name__=="__main__":
    game = kBandits(5)
    for i in range(5):
        print(f'Arm {i}')
        print(f'mean: {game.arms[i].mean}')
        print(f'std: {game.arms[i].std}')
        print(f'sample: {game.arms[i].sample()}')
        print(f'game pull: {game.pull(i)}')
        print()
