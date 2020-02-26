# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:14:42 2020

@author: cyclo
"""

from axelrod.strategies.finite_state_machines import FSMPlayer
from axelrod.action import Action
from axelrod import Tournament

import axelrod as axl

C, D = Action.C, Action.D




class ModifiedPeterson(FSMPlayer):
    
   name = "ModifiedPeterson"
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
            (1,C,1,C),
            (1,D,6,D),
            (2,C,2,D),
            (2,D,1,D),
            (3,C,3,C),
            (3,D,8,D),
            (4,C,4,C),
            (4,D,3,C),
            (5,C,5,C),
            (5,D,1,D),
            (6,C,2,C),
            (6,D,9,D),
            (7,C,2,C),
            (7,D,3,C),
            (8,C,6,D),
            (8,D,10,C),
            (9,C,4,C),
            (9,D,7,D),
            (10,C,5,D),
            (10,D,7,D),
            
        )

        super().__init__(
            transitions=transitions, initial_state=10, initial_action=C
        )

my = ModifiedPeterson()

players= [s() for s in axl.short_run_time_strategies]
players.append(my)
tournament=axl.Tournament(players)
results=tournament.play()
results.write_summary('Milestone4b.csv')
#plot=axl.Plot(results) 
#pl=plot.boxplot()
#pl.show()