import numpy as np

class EpsilonGreedyStruct:
    def __init__(self, num_arm, epsilon):
        self.d = num_arm
        self.epsilon = epsilon

        self.UserArmMean = np.zeros(self.d)
        self.UserArmTrials = np.zeros(self.d)

        self.time = 0

    def updateParameters(self, articlePicked_id, click):
        self.UserArmMean[articlePicked_id] = (self.UserArmMean[articlePicked_id]*self.UserArmTrials[articlePicked_id] + click) / (self.UserArmTrials[articlePicked_id]+1)
        self.UserArmTrials[articlePicked_id] += 1

        self.time += 1

    def getTheta(self):
        return self.UserArmMean

    def decide(self, pool_articles):
        if self.epsilon is None:
            explore = np.random.binomial(1, (self.time+1)**(-1.0/3))
            # explore = np.random.binomial(1, np.min([1, self.d/self.time]))
        else:
            explore = np.random.binomial(1, self.epsilon)
        if explore == 1:
            # print("EpsilonGreedy: explore")
            articlePicked = np.random.choice(pool_articles)
        else:
            # print("EpsilonGreedy: greedy")
            maxPTA = float('-inf')
            articlePicked = None

            for article in pool_articles:
                article_pta = self.UserArmMean[article.id]
                # pick article with highest Prob
                if maxPTA < article_pta:
                    articlePicked = article
                    maxPTA = article_pta

        return articlePicked

class EpsilonGreedyMultiArmedBandit:
    def __init__(self, num_arm, epsilon):
        self.users = {}
        self.num_arm = num_arm
        self.epsilon = epsilon
        self.CanEstimateUserPreference = False

    def decide(self, pool_articles, userID):
        if userID not in self.users:
            self.users[userID] = EpsilonGreedyStruct(self.num_arm, self.epsilon)

        return self.users[userID].decide(pool_articles)

    def updateParameters(self, articlePicked, click, userID):
        self.users[userID].updateParameters(articlePicked.id, click)

    def getTheta(self, userID):
        return self.users[userID].UserArmMean


