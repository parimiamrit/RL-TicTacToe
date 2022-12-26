import numpy as np

class safeagent(object):

    def __init__(self, playerid):
        self.playerid=playerid

    def action(self,board):
        for i in range(3):
            if(board[i][0]==board[i][1] and board[i][1]!=''):
                if(board[i][2]==''):
                    return [i,2]
            if(board[i][0]==board[i][2] and board[i][0]!=''):
                if(board[i][1]==''):
                    return [i,1]
            if(board[i][1]==board[i][2] and board[i][1]!=''):
                if(board[i][0]==''):
                    return [i,0]
        for i in range(3):
            if(board[0][i]==board[1][i] and board[1][i]!=''):
                if(board[2][i]==''):
                    return [2,i]
            if(board[0][i]==board[2][i] and board[0][i]!=''):
                if(board[1][i]==''):
                    return [1,i]
            if(board[1][i]==board[2][i] and board[1][i]!=''):
                if(board[0][i]==''):
                    return [0,i]
        if(board[0][0]==board[1][1] and board[1][1]!=''):
            if(board[2][2]==''):
                return [2,2]
        if(board[0][0]==board[2][2] and board[0][0]!=''):
            if(board[1][1]==''):
                return [1,1]
        if(board[1][1]==board[2][2] and board[1][1]!=''):
            if(board[0][0]==''):
                return [0,0]

        if(board[2][0]==board[1][1] and board[1][1]!=''):
            if(board[0][2]==''):
                return [0,2]
        if(board[2][0]==board[0][2] and board[2][0]!=''):
            if(board[1][1]==''):
                return [1,1]
        if(board[0][2]==board[1][1] and board[1][1]!=''):
            if(board[2][0]==''):
                return [2,0]

        p=np.random.randint(0,9)
        while(board[int(p/3),p%3]!=''):
            p=np.random.randint(0,9)
        return [int(p/3),p%3]
    
    def learn(self, reward, prev_state, state):
        return