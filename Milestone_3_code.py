"""
Math 285
Python Axelrod Game Theory
Name: Szu-Hung Hsiao (Nick Hsiao)
STD : 008717306
Milestone_2
"""

#==============================================================================
# Creating own strategies
#==============================================================================

import axelrod as axl
from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class IDoWhatIWant(Player):
    name = 'What I\'ve Done'
    '''
    This strategy start with cooperating with other.
    However, player will defect if the opponent defect 1/3 of previous time, 
    then will defect.
    More, if previous 2 times are both defect, then will defect.
    '''
    classifier = {
        "memory_depth": 0,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    def strategy(self, opponent: Player) -> Action:
        # First move start with (C)ooperate
        if not self.history:
            return C
        # Calculate the opponent's loyalty, if 1/3 of opponent history 
        #  is defected, then will defect as well
        if self.history:
            # Calculate the rate till previous term
            rate = list(opponent.history).count(D) / len(list(self.history))
            # Check (D)efect times and (C)ooperate times till previous round
            '''
            Below part is only for checking the number of times of C and D 
            each turn the strategy run
            
            t_of_D = list(opponent.history).count(D)
            t_of_C = len(self.history)-t_of_D
            # Total terms of previous round
            total_term = len(self.history)
            print(t_of_D,t_of_C,total_term, rate)
            print(rate)
            print(list(opponent.history))
            '''
            # First if statement if opponent history has more than 1/3 are D 
            #  then return D
            if rate >= 1/3:
                return D
            else:
                # After third round, if previous 2 times of opponent are D then
                #  return D if previous 3 times of opponent are C then return C
                if len(self.history) > 2:
                    if list(opponent.history)[-2] == D and list(opponent.history)[-1] == D:
                        return D
                    elif list(opponent.history)[-3:len(self.history)] ==[C, C, C]:
                        return C
                return C
        return C

#==============================================================================
# Tournament Running
#==============================================================================

# Store strategies that we need to test for the tornament into players
players = [IDoWhatIWant(), axl.Random(), axl.TitForTat(), axl.Defector(), axl.BackStabber(),
           axl.FirstByDavis(), axl.Grudger(), axl.Gambler(), axl.EvolvedLookerUp2_2_2(),
           axl.Cooperator()]

# Setting tournament with 200 turns and repetitions with 20
tournament = axl.Tournament(players, turns = 200, repetitions = 20)
# Run the tournament and save the result into results
results = tournament.play()
# Output the rank of choosen strategies
results.ranked_names

# Save results into csv file
results.write_summary('Milestone_3_result.csv')

# Save all results plots
plot = axl.Plot(results)
axl.Plot.save_all_plots(plot, 'Milestone_3', filetype = 'png')
