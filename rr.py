import random

class RussianRoulette(object):
    def __init__(self):
        self.chambers = [False]*6
        self.chambers[random.randint(0,5)] = True

    def trigger(self):
        try:
            return self.chambers.pop()
        except IndexError:
            return False