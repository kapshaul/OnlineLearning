import numpy as np

class UCBStruct:
    def __init__(self, num_arm, alpha):
        self.d = num_arm
        self.alpha = alpha

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
        maxPTA = float('-inf')
        articlePicked = None

        for article in pool_articles:
            if self.UserArmTrials[article.id] == 0:
                articlePicked = article
                return articlePicked
            else:
                article_pta = self.UserArmMean[article.id] + np.sqrt(2*self.alpha*np.log(self.time)/self.UserArmTrials[article.id])
                # pick article with highest Prob
                if maxPTA < article_pta:
                    articlePicked = article
                    maxPTA = article_pta

        return articlePicked

class UCBBandit:
    def __init__(self, num_arm, alpha):
        self.users = {}
        self.num_arm = num_arm
        self.alpha = alpha
        self.CanEstimateUserPreference = False

    def decide(self, pool_articles, userID):
        if userID not in self.users:
            self.users[userID] = UCBStruct(self.num_arm, self.alpha)

        return self.users[userID].decide(pool_articles)

    def updateParameters(self, articlePicked, click, userID):
        self.users[userID].updateParameters(articlePicked.id, click)

    def getTheta(self, userID):
        return self.users[userID].UserArmMean