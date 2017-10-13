
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

class Tic_tac:
    def __init__(self):
        self.empty = True
        self.opponent = False
        self.player = False

#creates a board of tic-tac blocks
class Board:
    def __init__(self):
        self.grid = [[0 for i in range(3)] for j in range(3)]
    def create_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = Tic_tac()    
    def move(self):
        best_val = -1000
        for i in range(3):
                for j in range(3):
                    if self.grid[i][j].empty:
                        self.grid[i][j].player = True
                        self.grid[i][j].empty = False
                        val = self.minimax(isPlayer = False)
                        self.grid[i][j].player = False
                        self.grid[i][j].empty = True
                        if(val > best_val):
                            best_move_i = i
                            best_move_j = j
                            best_val = val
        self.grid[best_move_i][best_move_j].player = True
        self.grid[best_move_i][best_move_j].empty = False
        print(best_move_i,best_move_j)
        
    def minimax(self, isPlayer):
        score = self.check_score()
        if score != 0:
            return(score)
        if self.check_end():
            return(0)
        
        if isPlayer:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j].empty:
                        self.grid[i][j].player = True
                        self.grid[i][j].empty = False
                        val = self.minimax(isPlayer = False)
                        best = max(best,val)
                        self.grid[i][j].player = False
                        self.grid[i][j].empty = True
                        
            return(best)

        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j].empty:
                        self.grid[i][j].opponent = True
                        self.grid[i][j].empty = False
                        val = self.minimax(isPlayer = True)
                        best = min(best,val)
                        self.grid[i][j].opponent = False
                        self.grid[i][j].empty = True
                        
            return(best)
        
    def check_end(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j].empty:
                    return False
        return True
    
    def check_score(self):
        #horizontal_case
        for i in range(3):
            size_opp = 0
            size_ply = 0
            for j in range(3):
                if self.grid[i][j].opponent:
                    size_opp += 1
                elif self.grid[i][j].player:
                    size_ply += 1
            if(size_opp == 3):
                return(-10)
            elif(size_ply == 3):
                return(10)

        #vertical_case
        for i in range(3):
            size_opp = 0
            size_ply = 0
            for j in range(3):
                if self.grid[j][i].opponent:
                    size_opp += 1
                elif self.grid[j][i].player:
                    size_ply += 1
            if(size_opp == 3):
                return (-10)
            elif(size_ply == 3):
                return (10)

        #diagonal_case
        size_opp = 0
        size_ply = 0
        for i in range(3):
            if self.grid[i][i].opponent:
                size_opp += 1
            elif self.grid[i][i].player:
                size_ply += 1
            if(size_opp == 3):
                return (-10)
            elif(size_ply == 3):
                return (10)

        #otherdiagonal_case
        size_opp = 0
        size_ply = 0
        for i in range(3):
            j = 2 - i
            if self.grid[i][j].opponent:
                size_opp += 1
            elif self.grid[i][j].player:
                size_ply += 1
            if(size_opp == 3):
                return (-10)
            elif(size_ply == 3):
                return (10)
        return(0)


# In[3]:

def myMove(row, col, board):
    board.grid[row][col].opponent = True
    board.grid[row][col].empty = False


# In[4]:

#initializes the instance
board = Board()


# In[5]:

#creates the board
board.create_grid()


# In[6]:

#example of a game
myMove(2,1, board)


# In[7]:

board.move()


# In[8]:

myMove(2,0, board)


# In[9]:

board.move()


# In[10]:

myMove(1,2, board)


# In[11]:

board.move()


# In[12]:

myMove(0,2, board)


# In[30]:

board.move()

