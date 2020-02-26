# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:35:41 2020

@author: cyclo
"""

import axelrod as axl
import numpy as np
import random


from axelrod.action import Action
from axelrod.player import Player



C, D = Action.C, Action.D


class AceHigh(Player):
    
   

    # These are various properties for the strategy
    name = "AceHigh"
    classifier = {
        "memory_depth": 0,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

   
    def strategy(self, opponent: Player) -> Action:
        spades=list(range(2,14))
        hearts=list(range(2,14))
        diamonds=list(range(2,14))
        clubs=list(range(2,14))
    
        draw1=random.choice(spades)
        draw2=random.choice(hearts)
        draw3=random.choice(diamonds)
        draw4=random.choice(clubs)
    
        draw5=random.choice(spades)
        draw6=random.choice(hearts)
        draw7=random.choice(diamonds)
        draw8=random.choice(clubs)
    
        hand1=np.sum([draw1,draw2,draw3,draw4])
        hand2=np.sum([draw5,draw6,draw7,draw8])
   

        if hand1+hand2>=25:
            return C
        else:
            return D
     
ah=AceHigh()    
players= [ah,axl.TitForTat(),axl.AdaptiveTitForTat(),axl.Defector(),axl.SecondByBlack(),axl.Punisher(),axl.Thumper()]
#players.append(ah)
tournament=axl.Tournament(players)
results=tournament.play()
results.write_summary('AceHigh.csv')
plot=axl.Plot(results) 
pl=plot.boxplot()
pl.show()
   


