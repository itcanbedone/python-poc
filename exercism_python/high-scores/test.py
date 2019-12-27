#!/usr/bin/env python

from high_scores import HighScores

#scores = [30, 50, 20, 70]
#print HighScores(scores).scores()

scores1 = [50, 30, 10]
print HighScores(scores1).personal_top()

scores2 = [20, 10, 30]
print HighScores(scores2).personal_top()

scores3 = [20, 40, 0, 30, 70]
print HighScores(scores3).report()

scores4 = [20, 100, 0, 30, 70]
print HighScores(scores4).report()
