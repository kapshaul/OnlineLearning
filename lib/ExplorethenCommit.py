import numpy as np

class ExplorethenCommitStruct:
    def __init__(self, num_arm, m):
        self.d = num_arm
        self.m = m

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
        if self.d*self.m < self.time:
            explore = 0
        else:
            explore = 1
        if explore == 1:
            article_index = int(self.time % self.d)
            articlePicked = pool_articles[article_index]
        else:
            maxPTA = float('-inf')
            articlePicked = None

            for article in pool_articles:
                article_pta = self.UserArmMean[article.id]
                # pick article with highest Prob
                if maxPTA < article_pta:
                    articlePicked = article
                    maxPTA = article_pta

        return articlePicked

class ExplorethenCommit:
    def __init__(self, num_arm, m):
        self.users = {}
        self.num_arm = num_arm
        self.m = m
        self.CanEstimateUserPreference = False

    def decide(self, pool_articles, userID):
        if userID not in self.users:
            self.users[userID] = ExplorethenCommitStruct(self.num_arm, self.m)

        return self.users[userID].decide(pool_articles)

    def updateParameters(self, articlePicked, click, userID):
        self.users[userID].updateParameters(articlePicked.id, click)

    def getTheta(self, userID):
        return self.users[userID].UserArmMean


