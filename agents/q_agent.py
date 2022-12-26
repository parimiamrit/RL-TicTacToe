import numpy as np
from collections import defaultdict
import random

class qagent(object):
    
    def __init__(self, playerid, epsilon=0.05, alpha=0.9, gamma=0.99):
        self.playerid = playerid
        self.latest_action = [-1,-1]
        self.epsilon=epsilon
        self.alpha=alpha
        self.gamma=gamma
        self.q=defaultdict(lambda: 0)

    def Q(self, s, a):
        return self.q[str([s,a])]
    
    def available_actions(self, board):
        return np.argwhere(board=='')

    def action(self, board, train=True):
        if train:
            g=random.random()
            if g < self.epsilon:
                actions = self.available_actions(board)
                p=np.random.randint(0,len(actions))
                self.latest_action = actions[p]
                return self.latest_action
            else:
                if(len(np.argwhere(board=='')[0])==None):
                    self.latest_action = None
                    return None
                else:
                    self.latest_action = self.policy(board)
                    return self.latest_action
        else:
            self.latest_action = self.greedychoice(board)
            return self.latest_action

    def greedychoice(self, board):
        if(len(np.argwhere(board=='')[0])==None):
            return None
        else:
            return self.policy(board)
    
    def learn(self, reward, prev_state, state):
        self.updateQ(prev_state, self.latest_action, reward)
        return

    def policy(self, board):
        kx=np.argwhere(board=='')
        max_value=max(self.Q(board,a) for a in kx )
        max_actions=[a for a in kx if self.Q(board,a)==max_value]
        return random.choice(max_actions)


    def updateQ(self, s, a, r):
        sp,s=s.copy(),s.copy()
        sp[a]=='X'
        kx=np.argwhere(sp=='')
        if(len(kx)==0):
            max_value=None
            max_actions=None
            ap=None
        else:
            max_value=max([self.Q(sp,ac) for ac in kx])
            max_actions=[ac for ac in kx if self.Q(sp,ac)==max_value]
            ap = random.choice(max_actions)
        self.q[str([s,a])]=self.Q(s,a)+self.alpha*(r+self.gamma*self.Q(sp,ap)-self.q[str([s,a])])