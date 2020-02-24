import axelrod as axl
import Rochambeau as m
import MindTheGap as c

mine = [m.Rochambeau(), c.MindTheGap()]
players = [s() for s in axl.short_run_time_strategies] + mine
tournament = axl.Tournament(players, turns=10, repetitions=3)
results = tournament.play(processes=0)

results.write_summary('summary.csv')
import csv
with open('summary.csv', 'r') as outfile:
    csvreader = csv.reader(outfile)
    for row in csvreader:
        print(row)
