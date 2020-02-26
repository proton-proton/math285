# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:56:20 2020

@author: cyclo
"""

from axelrod.strategies.finite_state_machines import FSMPlayer
from axelrod.action import Action
from axelrod import Tournament

import axelrod as axl

C, D = Action.C, Action.D




class K4(FSMPlayer):
    
   name = "K4"
   classifier = {
        "memory_depth": 1, #or 2 or more idk
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
   def __init__(self) -> None:
        transitions = (
           (0, C, 0, C),
            (0, D, 2, D),
            (1, C, 3, D),
            (1, D, 0, C),
            (2, C, 2, D),
            (2, D, 1, C),
            (3, C, 3, D),
            (3, D, 1, D),
        )

        super().__init__(
            transitions=transitions, initial_state=1, initial_action=C
        )

my = K4()

players= [s() for s in axl.short_run_time_strategies]
players.append(my)
tournament=axl.Tournament(players)
results=tournament.play()
results.write_summary('Milestone4d.csv')
plot=axl.Plot(results) 
pl=plot.boxplot()
pl.show()