import numpy as np

class DiscountedUCBStruct:
    def __init__(self, num_arm, alpha, gamma):
        self.d = num_arm
        self.alpha = alpha
        self.gamma = gamma

        self.UserArmMean = np.zeros(self.d)
        self.DisUserArmTrials = np.zeros(self.d)

        self.time = 0

    def updateParameters(self, articlePicked_id, click):
        self.UserArmMean[articlePicked_id] = (self.gamma*(self.UserArmMean[articlePicked_id]*self.DisUserArmTrials[articlePicked_id]) + click) / (self.gamma*self.DisUserArmTrials[articlePicked_id] + 1)
        self.DisUserArmTrials[articlePicked_id] = self.gamma*self.DisUserArmTrials[articlePicked_id] + 1

        self.time += 1

    def getTheta(self):
        return self.UserArmMean

    def decide(self, pool_articles):
        maxPTA = float('-inf')
        articlePicked = None

        for article in pool_articles:
            if self.DisUserArmTrials[article.id] == 0:
                articlePicked = article
                return articlePicked
            else:
                article_pta = self.UserArmMean[article.id] + np.sqrt(2*self.alpha*np.log(self.time)/self.DisUserArmTrials[article.id])
                # pick article with highest Prob
                if maxPTA < article_pta:
                    articlePicked = article
                    maxPTA = article_pta

        return articlePicked

class DiscountedUCBBandit:
    def __init__(self, num_arm, alpha, gamma):
        self.users = {}
        self.num_arm = num_arm
        self.alpha = alpha
        self.gamma = gamma
        self.CanEstimateUserPreference = False

    def decide(self, pool_articles, userID):
        if userID not in self.users:
            self.users[userID] = DiscountedUCBStruct(self.num_arm, self.alpha, self.gamma)

        return self.users[userID].decide(pool_articles)

    def updateParameters(self, articlePicked, click, userID):
        self.users[userID].updateParameters(articlePicked.id, click)

    def getTheta(self, userID):
        return self.users[userID].UserArmMean