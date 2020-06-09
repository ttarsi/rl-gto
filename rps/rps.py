from players import RPSStaticPlayer
        
class RPS:
    def __init__(self, player1, player2):
        player1.wins = 0
        player2.wins = 0
        self.player1 = player1 
        self.player2 = player2

    def shoot(self):
        action1 = self.player1.action()
        action2 = self.player2.action()
        self.evaluate(action1, action2)

    def evaluate(self, action1, action2):
        if action1 == action2:
            return
        elif action1 == "rock":
            if action2 == "scissors":
                return self.player1.win()
            elif action2 == "paper":
                return self.player2.win()
        elif action1 == "paper":
            if action2 == "rock":
                return self.player1.win()
            elif action2 == "scissors":
                return self.player2.win()
        elif action1 == "scissors":
            if action2 == "paper":
                return self.player1.win()
            elif action2 == "rock":
                return self.player2.win()

    def simulate(self):
        print(f'{self.player1.name}  vs.  {self.player2.name}')
        for i in range(100000):
            self.shoot()
            if (i + 1) % 10000 == 0 and True:
                print(f'After {i+1} rounds:')
                print(f'    Player 1: {self.player1.wins} wins')
                print(f'    Player 2: {self.player2.wins} wins')
        print()
        print(f'{self.player1.name} won {round(self.player1.wins / (self.player1.wins + self.player2.wins) * 100, 2)} % of games vs. {self.player2.name}')


if __name__=="__main__":
    p1 = RPSStaticPlayer("balanced", 0.33, 0.33, 0.33) 
    p2 = RPSStaticPlayer("aggro", 0.5, 0.1, 0.4)
    game = RPS(p1, p2)
    game.simulate()
