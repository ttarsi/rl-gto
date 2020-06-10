import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

from game import kBandits
from players import GreedyBandit, GreedyBandit2


def main():
    k = 10 
    game = kBandits(k)
    print([k.mean for k in game.arms])
    player = GreedyBandit(k)
    player2 = GreedyBandit2(k)
    for i in tqdm(range(10000)):
        arm = player.choose() 
        reward = game.pull(arm)
        player.add_reward(arm, reward) 

        arm2 = player2.choose()
        reward2 = game.pull(arm2)
        player2.add_reward(arm2, reward2) 

    plt.plot(np.cumsum(player.rewards), label="Greedy Player 1")
    plt.plot(np.cumsum(player2.rewards), label="Greedy Player 2")
    plt.xlabel("t")
    plt.ylabel("cumulative reward")
    plt.legend()
    plt.savefig("greedy_comparison.png")


if __name__=="__main__":
    main()
