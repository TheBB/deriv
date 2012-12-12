class Game:

    def __init__(self, order, historySize):
        self.order = order
        self.history = [0] * historySize
        self.cDerivatives = [0] * (order+1)
        self.pDerivatives = self.cDerivatives

    def tick(self, control, deltaT):
        self.cDerivatives[self.order] = control
        for i in range(self.order,0,-1):
            self.cDerivatives[i-1] = self.pDerivatives[i-1] + 0.5*deltaT*(self.pDerivatives[i] + self.cDerivatives[i])
        self.pDerivatives = self.cDerivatives
        self.history.append(self.cDerivatives[0])
        self.history.pop(0)
