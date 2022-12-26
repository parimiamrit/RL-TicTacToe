import numpy as np

def all_same(arr,val):
    return all(ele == val for ele in arr)

'''Environment for the game TicTacToe'''
class TicTacToe(object):

    def __init__(self):
        self.board=np.array([['','',''],['','',''],['','','']])
        self.winner=None
        self.reward=0
        self.end = False
    
    def reset(self):
        self.board=np.array([['','',''],['','',''],['','','']])
        self.winner=None
        self.reward=0
        self.end = False

    def endgame(self):
        rewards = {'X':10, 'O':-10, 'D':-1}
        
        for i in range(3):
            if(all_same(self.board[i],'X') or all_same(self.board[i],'O')):
                self.winner=self.board[i,0]
                self.reward = rewards[self.winner]
                self.end = True
                return True

        for i in range(3):
            if(all_same(self.board[:,i],'X') or all_same(self.board[:,i],'O')):
                self.winner=self.board[0,i]
                self.reward = rewards[self.winner]
                self.end = True
                return True

        diag = [self.board[0,0],self.board[1,1],self.board[2,2]]
        if(all_same(diag,'X') or all_same(diag,'O')):
            self.winner=self.board[1,1]
            self.reward = rewards[self.winner]
            self.end = True
            return True
        
        diag = [self.board[2,0],self.board[1,1],self.board[0,2]]
        if(all_same(diag,'X') or all_same(diag,'O')):
            self.winner=self.board[1,1]
            self.reward = rewards[self.winner]
            self.end = True
            return True
        
        if '' not in self.board.flatten():
            self.winner = 'D'
            self.reward = rewards[self.winner]
            self.end = True
            return True
        else:
            self.reward = 0
            self.end = False
            return False

    
    def act(self,action,playerid):
        self.board[action[0],action[1]]=playerid
        self.endgame()
        return

    def print_board(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i,j]==''):
                    print(" ", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()
        print()

    def state(self):
        return self.board
