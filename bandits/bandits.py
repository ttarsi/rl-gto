import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

from game import kBandits
from players import GreedyBandit, GreedyBandit2, EpsGreedyBandit


def main():
    k = 10
    game = kBandits(k)

    print("Arm means:")
    print([k.mean for k in game.arms])

    players = [
        GreedyBandit(k),
        GreedyBandit2(k),
        EpsGreedyBandit(k, epsilon=0.5),
        EpsGreedyBandit(k, epsilon=0.1),
        EpsGreedyBandit(k, epsilon=0.01),
    ]

    for i in tqdm(range(20000)):
        for p in players:
            arm = p.choose()
            reward = game.pull(arm)
            p.add_reward(arm, reward)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,12))
    for p in players:
        cum_rewards = np.cumsum(p.rewards)
        mean_rewards = cum_rewards / np.arange(1, len(cum_rewards) + 1)
        ax1.plot(cum_rewards, label=p.name)
        ax2.plot(mean_rewards, label=p.name)
    ax1.set_xlabel("t")
    ax2.set_xlabel("t")
    ax1.set_ylabel("cumulative reward", fontsize=16)
    ax2.set_ylabel("mean reward", fontsize=16)
    ax1.legend()
    ax2.legend()
    plt.savefig("greedy_comparison.png")


if __name__=="__main__":
    main()
