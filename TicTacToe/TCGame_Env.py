#from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product
import copy

class TicTacToe():

    def __init__(self):
        #"""initialise the board"""
        
        # initialise state as an array
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix

        self.reset()

    def is_winning(self, curr_state):
        # """Takes state as an input and returns whether any row, column or diagonal has winning sum
        # Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        # Output = False"""

        # "check for the top row , diagonal and left column"
        
        #Identify the winning state based on various winning combination
        
        tmp_curr_state = np.array(curr_state)
        tmp_curr_state = np.where(tmp_curr_state=='nan',0,tmp_curr_state)
        
        if (tmp_curr_state[0]+tmp_curr_state[1]+tmp_curr_state[2] == 15) and (tmp_curr_state[0] != 0 and tmp_curr_state[1] != 0 and tmp_curr_state[2] != 0):
            return True
        elif tmp_curr_state[0]+tmp_curr_state[4]+tmp_curr_state[8] == 15 and  (tmp_curr_state[0] != 0 and tmp_curr_state[4] != 0 and tmp_curr_state[8] != 0):
            return True
        elif tmp_curr_state[0]+tmp_curr_state[3]+tmp_curr_state[6] == 15 and  (tmp_curr_state[0] != 0 and tmp_curr_state[3] != 0 and tmp_curr_state[6] != 0):
            return True
        elif tmp_curr_state[1]+tmp_curr_state[4]+tmp_curr_state[7] == 15 and (tmp_curr_state[1] != 0 and tmp_curr_state[4] != 0 and tmp_curr_state[7] != 0):  #"check for second column"
            return True
        elif tmp_curr_state[2]+tmp_curr_state[4]+tmp_curr_state[6] == 15 and (tmp_curr_state[2] != 0 and tmp_curr_state[4] != 0 and tmp_curr_state[6] != 0): #"check for diagonal and third column"
            return True
        elif (tmp_curr_state[2]+tmp_curr_state[5]+tmp_curr_state[8] == 15) and (tmp_curr_state[2] != 0 and tmp_curr_state[5] != 0 and tmp_curr_state[8] != 0):
            return True
        elif (tmp_curr_state[3]+tmp_curr_state[4]+tmp_curr_state[5] == 15) and (tmp_curr_state[3] != 0 and tmp_curr_state[4] != 0 and tmp_curr_state[5] != 0): #"check for second row"
            return True  
        elif (tmp_curr_state[6]+tmp_curr_state[7]+tmp_curr_state[8] == 15) and (tmp_curr_state[6] != 0 and tmp_curr_state[7] != 0 and tmp_curr_state[8] != 0): #"check for the bottom row"
            return True
        else:
            return False

 

    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up
        
        if self.is_winning(curr_state) == True:
            return True
        elif len(self.allowed_positions(curr_state)) ==0:
            return True
        else:
            return False

    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        curr_state[curr_action[0]] = curr_action[1] #"Update the state with the current action"
        return curr_state


    def step(self, curr_state, curr_action):
        # """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        # agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        # Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        # Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        
        #---------------Agents move------------------------------------
        curr_state =  self.state_transition(curr_state,curr_action) #"Get the state after the agents action"
        if (self.is_winning(curr_state)):  #"check if the agents is winning"
            return (curr_state ,10 ,True)
        if self.is_terminal(curr_state): #"Check if the game is terminal"
            return (curr_state,0,True)
        #---------------Environments  move------------------------------------
        env_actions = [i for i in self.action_space(curr_state)[1]]            #"Get available actions for the environment"
        s_action = random.randrange (0,len(env_actions))        #"choose a random environment action"
        curr_state = self.state_transition(curr_state,env_actions[s_action])  #"perform the environments action"

        if (self.is_winning(curr_state)):                        #"Check if the environment is winning"
            return (curr_state ,-10 ,True)
        
        if self.is_terminal(curr_state):                        #"check if the game is terminal after environments action"
            return (curr_state,0,True)

        return (curr_state,-1,False)                        #"Default for actions"


    def reset(self):
        return self.state


