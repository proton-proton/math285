# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:11:03 2020

@author: cyclo
"""
from axelrod.strategies.finite_state_machines import FSMPlayer
from axelrod.action import Action
from axelrod import Tournament

import axelrod as axl

C, D = Action.C, Action.D




class Mycleskian(FSMPlayer):
    
   name = "Mycleskian"
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
            (1,C,2,D),
            (1,D,3,D),
            (2,C,9,C),
            (2,D,6,C),
            (3,C,5,C),
            (3,D,8,C),
            (4,C,2,D),
            (4,D,10,C),
            (5,C,4,C),
            (5,D,7,C),
            (6,C,11,C),
            (6,D,3,D),
            (7,C,1,C),
            (7,D,7,D),
            (8,C,11,C),
            (8,D,4,C),
            (9,C,11,C),
            (9,D,5,C),
            (10,C,1,C),
            (10,D,10,D),
            (11,C,7,C),
            (11,D,10,C)
        )

        super().__init__(
            transitions=transitions, initial_state=10, initial_action=C
        )

my = Mycleskian()

players= [s() for s in axl.short_run_time_strategies]
players.append(my)
tournament=axl.Tournament(players)
results=tournament.play()
results.write_summary('Milestone4.csv')
plot=axl.Plot(results) 
pl=plot.boxplot()
pl.show()
