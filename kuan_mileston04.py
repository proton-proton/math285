"""
Name: Kuan-Lin Chen
Assignment: Milestone 4
Class: MATH 285
Instructor: Dr. Fryer
Date: 2/22/2020
"""

import axelrod as axl

from collections import namedtuple
from typing import TypeVar
from axelrod.action import Action
from axelrod.strategies import LookerUp

C, D = Action.C, Action.D
actions = (C, D)

Plays = namedtuple("Plays", "self_plays, op_plays, op_openings")
Reaction = TypeVar("Reaction", Action, float)


class New_Stuff_Winner22(LookerUp):
    """
    A lookup table based strategy.
    Names:
    - Winner22
    """

    name = "Winner22"

    def __init__(self) -> None:
        params = Plays(self_plays=2, op_plays=2, op_openings=0)
        pattern = "CDCDDCDCCDDCCDCC"
        super().__init__(parameters=params, pattern=pattern, initial_actions=(C,))


        
        
players = [s() for s in axl.short_run_time_strategies]  # initialize players
players.append(New_Stuff_Winner22())  # add new built class into players
tournament = axl.Tournament(players)  # initialize a tournament
results = tournament.play()           # start the tournament

# save the plots in png files
plot = axl.Plot(results)
plot.save_all_plots(prefix = "mileston04", filetype = "png")

# put the result of the tournament in csv file 
results.write_summary('milestone04_summary.csv')