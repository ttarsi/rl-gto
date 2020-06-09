from players import RPSStaticPlayer
from game import RPS

def main():
    p1 = RPSStaticPlayer("balanced", 0.33, 0.33, 0.33) 
    p2 = RPSStaticPlayer("aggro", 0.5, 0.1, 0.4)
    game = RPS(p1, p2)
    game.simulate()

if __name__=="__main__":
    main()
