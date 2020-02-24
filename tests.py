import axelrod as axl
import Rochambeau as m
import MindTheGap as c
import rose as r
import kuan as k
import MW as w
import cord1 as o



mine = [m.Rochambeau(), c.MindTheGap(), r.rose(), k.kuan(), w.MW(), o.cord1(), o.cord2(), o.cord3(), o.cord4(), o.cord5()]
players = [s() for s in axl.short_run_time_strategies] + mine
tournament = axl.Tournament(players, turns=10, repetitions=3)
results = tournament.play(processes=0)


results.write_summary('summary_new.csv')
import csv
with open('summary_new.csv', 'r') as outfile:
    csvreader = csv.reader(outfile)
    for row in csvreader:
        print(row)


"""
mine = [m.Rochambeau(), c.MindTheGap(), r.rose(), k.kuan]
players = [s() for s in axl.short_run_time_strategies] + mine
players = (m.Rochambeau(), c.MindTheGap(), r.rose())
players = (m.Rochambeau(), c.MindTheGap(), r.rose())
tournament = axl.Tournament(players, turns=10, repetitions=3)
results = tournament.play(processes=0)



plot = axl.Plot(results)
p = plot.winplot()
p.show()

p = plot.payoff()
p.show()

mine = [m.Rochambeau(), c.MindTheGap(), r.rose()]
players = [s() for s in axl.short_run_time_strategies] + mine


results.write_summary('summary.csv')
import csv
with open('summary.csv', 'r') as outfile:
    csvreader = csv.reader(outfile)
    for row in csvreader:
        print(row)
"""