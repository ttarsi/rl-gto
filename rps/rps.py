from players import RPSStaticPlayer
        
class RPS:
    def __init__(self, player1, player2):
        self.player1 = player1 
        self.player2 = player2

    def shoot(self):
        action1 = self.player1.action()
        action2 = self.player2.action()
        self.evaluate(action1, action2)

    def evaluate(self, action1, action2):
        if action1 == action2:
            return -1
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
        elif action1 == "rock":
            if action2 == "scissors":
                return self.player1.win()
            elif action2 == "paper":
                return self.player2.win()
            
if __name__=="__main__":
    p1 = RPSStaticPlayer("balanced", 0.33, 0.33, 0.33) 
    p2 = RPSStaticPlayer("aggro", 0.50, 0.10, 0.40) 
    game = RPS(p1, p2)
    print(f'{p1.name}  vs.  {p2.name}')
    for i in range(100000):
        game.shoot() 
        if (i + 1) % 10000 == 0:
            print(f'After {i+1} rounds:')
            print(f'    Player 1: {p1.wins} wins')
            print(f'    Player 2: {p2.wins} wins')
    print()
    print(f'{p1.name} won {round(p1.wins / (p1.wins + p2.wins) * 100, 2)} % of games vs. {p2.name}')


