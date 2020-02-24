# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:02:33 2020

@author: mitch
"""

from axelrod.strategies.finite_state_machines import FSMPlayer
from axelrod.action import Action
from axelrod import Tournament

import axelrod as axl

C, D = Action.C, Action.D

class TriForce(FSMPlayer):
    
    name = "TriForce"
    classifier = {
        "memory_depth": 1,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    
    def __init__(self) -> None:
        transitions = (
            (1, C, 4, C),
            (1, D, 2, D),
            (2, C, 4, D),
            (2, D, 3, D),
            (3, C, 2, D),
            (3, D, 3, D),
            (4, C, 6, C),
            (4, D, 5, C),
            (5, C, 2, C),
            (5, D, 3, D),
            (6, C, 6, C),
            (6, D, 5, C)
        )

        super().__init__(
            transitions=transitions, initial_state=1
        )
        

tf = TriForce() #Create instance of class

players = [s() for s in axl.short_run_time_strategies]  # Create players

players.append(tf)
tournament = Tournament(players)  # Create a tournament
results = tournament.play()  # Play the tournament

results.write_summary('SummaryMileStone4-1.csv') # Write results to csv file

plot = axl.Plot(results)
p = plot.boxplot() #Plot results 
p.show()