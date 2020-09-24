# Import routines

import numpy as np
import math
import random
from gym import spaces
from sklearn.preprocessing import OneHotEncoder


# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        #"""initialise your state and define your action space and state space"""
        self.action_space = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(1,3),(1,4),(2,0),(2,1),(2,3),(2,4),(3,0),(3,1),(3,2),(3,4),(4,0),(4,1),(4,2),(4,3)]
        
        self.location = np.random.choice(np.arange(0,m-1))
        self.day = np.random.choice(np.arange(0,d-1))
        self.time = np.random.choice(np.arange(0,t-1))

        self.state_space = [(x,y,z) for x in range (0,m) for y in range (0,d) for z in range(0,t)]
        self.state_init = (self.location,self.time,self.day)

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        #covert the number into encoded format for the NN
        locs = np.zeros(m)
        time = np.zeros(t)
        day = np.zeros(d)

        locs[int(state[0])] = 1
        time[int(state[1])] = 1
        day[int(state[2])] = 1

        state_encod = np.concatenate((locs,time,day), axis=None) #flatten the array into a vector 
        return state_encod


    # Use this function if you are using architecture-2 
    # def state_encod_arch2(self, state, action):
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        
    #     return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        requests = 0
        if location == 0:
            requests = np.random.poisson(2)
        elif location ==1:
            requests = np.random.poisson(12)
        elif location ==2:
            requests = np.random.poisson(4)
        elif location ==3:
            requests = np.random.poisson(7)
        elif location ==4:
            requests = np.random.poisson(8)


        if requests >15:
            requests =15

        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]
      
        possible_actions_index.append(20)
        actions.append((0,0))

        return possible_actions_index,actions   



    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        #Get the current state and action
        #check if the current action is (0,0)
        # if yes then reward is -c i.e cost of the fuel for one hour before it gets another customer
        # if no , then check is the current location is same as the action (start loc)
        #       if yes , then calculate the time from time matrix and calculate the reward based on the current trip
        #       if no , then calculate the fuel cost (hence time from time matrix) to go to the pick up point from the current state (loc)
        #               then calculate the fuel cost and revenue for the trip and cancluate the reward accordingly
        
        flag_action = False
        trip_time = 0
        empty_time = 0
        reward = 0
        if int(action[0]) == 0 and int(action[1]) == 0:
            flag_action = True

        # action (0,0)
        if flag_action:
            reward = -C
        else:
            #check if the pick up locations and current location is same
            if state[0] == action[0]:
                trip_time = Time_matrix[action[0]][action[1]][state[1]][state[2]]
            else:
                empty_time = Time_matrix[state[0]][action[0]][state[1]][state[2]]
                time_change = self.add_time(state[0], action[0], state[1], state[2], Time_matrix)
                trip_time =  Time_matrix[int(action[0])][int(action[1])][int(time_change[0])][int(time_change[1])]
            
            reward = int(R * trip_time - (C * (empty_time + trip_time)))

        return reward




    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        #Get the current state and action
        #check if the current action is (0,0), 
        # if yes then only increment the time by an hour. Increment the day if the time exeeds 24
        # if no, then the state will have the location as mentioned in the action (destination)
        #           increment the time based on the data in the time matrx, increment the day if time exeeds 24 hrs

        flag_action = False
        if action[0] == 0 and action[1] == 0:
            flag_action = True
        
        if flag_action:
            time_next = state[1] + 1
            day_next = state[2]
            loc_next = state[0]
        else:
            # Check is the current state position and start position for the action is same. 
            #   If it is same then the time from action-start to action-end needs to be calculated from the time matrix
                # Add the state[time] with the value 
            #   If it si not same , then calculate the time from state position to action[start pos] and then from action [start pos] to action [end pos]
            #   #Add the state[time] with both the values 
            if state[0] == action[0]:
                newtime = self.add_time(action[0], action[1], state[1], state[2], Time_matrix)
                time_next = newtime[0]
                day_next = newtime[1]
                loc_next = action[1]
            else:
                newtime = self.add_time(state[0], action[0], state[1], state[2], Time_matrix)
                droptime = self.add_time(action[0], action[1], newtime[0], newtime[1], Time_matrix)
                time_next = droptime[0]
                day_next = droptime[1]
                loc_next = action[1]
        
        if  time_next > 23: 
            time_next = 0
            day_next += 1
        if day_next > 6:
            day_next = 0

        return (int(loc_next), int(time_next), int(day_next))

    def add_time(self, start, end ,time ,day, Time_matrix ):
            currtime = time + Time_matrix[int(start)][int(end)][int(time)][int(day)]
            currday = day
            if currtime > 23:
                currtime = currtime - 24
                currday = day + 1
                if currday > 6:
                    currday = currday - 7
            return (currtime,currday) 



    def reset(self):
        return self.action_space, self.state_space, self.state_init
