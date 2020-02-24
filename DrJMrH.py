# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:36:58 2020

@author: mitch
"""

import random

from axelrod.player import Player
from axelrod.action import Action
from axelrod import Tournament

import axelrod as axl

C, D = Action.C, Action.D

class DrJekyllMrHyde(Player):
    
    name = "Dr. Jekyll and Mr. Hyde"
    classifier = {
        "memory_depth": 2,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    
    def strategy(self, opponent: Player) -> Action:
        
        #Keep track of opponents previous two moves
        if len(opponent.history) == 0:
            opponent_first_previous = 0
            opponent_second_previous = 0

        
        elif len(opponent.history) == 1:
            opponent_first_previous = 1 if opponent.history[-1] == C else 0
            opponent_second_previous = 0
    
        else:
            opponent_first_previous = 1 if opponent.history[-1] == C else 0
            opponent_second_previous = 1 if opponent.history[-2] == C else 0
        
        #Strarting move is Cooperate
        if len(self.history) == 0:
            return C
        
        #If opponent shows trend of Cooperation then cooperate
        elif opponent_first_previous == 1 and opponent_second_previous == 1:
            return C
        
        #If opponent shows trend of Defection then defect
        elif opponent_first_previous == 0 and opponent_second_previous == 0:
            return D
        
        else:
            #Random value for Mr Hyde
            h = random.random()
            #Random value for Dr Jykle
            j = random.random()
            #Let Mr Hyde and Dr Jykle compete 
            #If Dr Jykle beats Mr Hyde cooperate else defect
            if h - j >= 0:
                return C
            else:
                return D

hj = DrJekyllMrHyde() #Create instance of class

#players = [s() for s in axl.short_run_time_strategies]  # Create players
players = [hj, axl.Defector(), axl.TitForTat(), axl.Thumper(), axl.Punisher(), axl.AdaptiveTitForTat(), axl.FirstByDavis(), axl.Appeaser()]
#players.append(hj)
tournament = Tournament(players)  # Create a tournament
results = tournament.play()  # Play the tournament

results.write_summary('SummaryMileStone3.csv') # Write results to csv file

plot = axl.Plot(results)
p = plot.boxplot() #Plot results 
p.show()