import numpy as np

class randomagent(object):
    
    def __init__(self, playerid):
        self.playerid=playerid
        self.latest_action = [-1,-1]

    def action(self, board, train=True):
        p=np.random.randint(0,9)
        while(board[int(p/3),p%3]!=''):
            p=np.random.randint(0,9)
        self.latest_action = [int(p/3),p%3]
        return self.latest_action
    
    def learn(self, reward, prev_state, state):
        return