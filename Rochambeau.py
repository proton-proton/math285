from axelrod.action import Action
from axelrod.player import Player
import axelrod as axl
import random

C, D = Action.C, Action.D

class Rochambeau(Player):
    """A player who plays a game of "Rock Paper Scissors" with itself to decide
    the action it will take.  This particular strategy is equivalent to rand, performance wise.

    Fun Fact:  The name "Rochambeau" is commonly used on the west coast, particularly in
    Northern California.  It is frequently mistaken as the french name for the game, but this is entirely untrue.
    Some people claim that this term is linked to a french general in the revolutionary war, Comte de Rochambeau.
    However, the first time "Rochambeau" appeared in print was an Oakland publication in 1936.  There is no real
    connection to the game and the man.

    What is most likely what happened also explains the bay area origins.  The game itself was created in China, and
    spread to Japan.  The Japanese name of the game is "Jon Ken Pon".  Immigration from Asian countries created specific
    demographics in the bay, resulting in large east asian communities.  Children of these immigrants brought the game with them,
    which explains the first mention of the game in print in the 1930s.  Bay area kids likely americanized it into a variation of
    "Ro Sham Bo", mirroring the "Jon Ken Pon" syllable cadence.  Generations pass, and kids are still playing the game, but time
    has distanced them from the origins and original name.  They have always said "Roshambo", but one day someone assumed it had
    a french spelling, and voila!  "Rochambeau"!

    source:https://www.mentalfloss.com/article/80201/why-do-people-call-rock-paper-scissors-roshambo
    """

    name = "Rochambeau"
    classifier = {
        "memory_depth": 0,
        "stochastic": True,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }



    def strategy(self, opponent: Player) -> Action:

        Move = ['R', 'P', 'S']  # gameplay options

         # Player1 - she always wants to cooperate
          # Player 2 - she always wants to defect

        P1 = random.choice(Move)
        P2 = random.choice(Move)

        if P1 == P2: #ties register as C to make it slightly biased
            return C
        if P1 == 'R'  and P2 == 'P':  # defect cases
            return D
        if P1 == 'P' and P2 == 'S':
            return D
        if P1 == 'S' and P2 == 'R':
          return D
        else:
           return C  # all else C


players = (Rochambeau(), axl.TitForTat())
match = axl.Match(players, 5)
interactions = match.play()
print(interactions)