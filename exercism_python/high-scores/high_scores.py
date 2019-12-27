class HighScores(object):
    def __init__(self, scores):
        self.high_scores = scores

    @property
    def scores(self):
        return self.high_scores


    def latest(self):
        return self.high_scores[-1]

    def personal_best(self):
        return max(self.high_scores)

    def personal_top(self):
        self.high_scores.sort(reverse=True)
        top_scores = self.high_scores[0:3]
        return top_scores

    def report(self):
        if self.personal_best() == self.latest():
            report = "Your latest score was {}. That's your personal best!".format(self.latest())
        else:
            report = "Your latest score was {}. That's {} short of your personal best!".format(self.latest(),
                                                                                               self.personal_best() - self.latest())

        return report
