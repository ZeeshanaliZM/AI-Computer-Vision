#To solve 8 Puzzle Problem using Greedy Best First Search Algorithm
#This Searching algorithm is an Informed Search Algorithm since we have information about the number of tiles that are misplaced
#It is a pure heurestic algorithm as the cost function only depends on the number of misplaced tiles expect the empty tile
#The position of each tile in the queue is determined by its heurestic value which is the number of misplaced tiles
#Hence the queue used is a priority queue
import numpy as np
from copy import deepcopy

#Declare each state as having a value and the link to each parent state
class State:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.heurestic = 0

#Declare the class to intialize the depth first search tree
class Greedy_Best_Search:
    def __init__(self,initial,goal):
        self.start = State(initial,None)
        self.goal = goal
        self.start.heurestic = self.heurestic_value(self.start)
        self.path = []
        self.visited = []
        self.priority_queue = []
        self.GBFS()

#To locate the position of the zeros in each state
    def find_zeros(self,current):
        return np.where(current.value==0)
    
    def heurestic_value(self,state):
        diff = state.value - self.goal
        count = np.count_nonzero(diff)
        return count-1

#This function is used to ensure no repeatitive states occur in the stack. 
    def list_present(self,list_check,current):
        for i in list_check:
            if((current.value==i.value).all()==True):
                return True
        else:
            return False

#This function is used to add the next states to the queue in order of their heurestic function
#The states are given priority based o their heurestic function
    def add_to_priority_queue(self,current):
        for i in range(len(self.priority_queue)):
            if i==0 and current.heurestic<=self.priority_queue[0].heurestic:
                self.priority_queue.insert(0,current)
                return
            elif i==len(self.priority_queue)-1:
                self.priority_queue.append(current)
                return
            else:
                small = self.priority_queue[i].heurestic
                large = self.priority_queue[i+1].heurestic
                if (small<=current.heurestic and large>=current.heurestic):
                    self.priority_queue.insert(i+1,current)
                    return

#Function that checks and moves the zero to the right if possible
    def move_right(self,current):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (col<2):
            temp.value[row,col+1] = current.value[row,col]
            temp.value[row,col] = current.value[row,col+1]
            temp.heurestic = self.heurestic_value(temp)
            check1 = self.list_present(self.priority_queue,temp)
            check2 = self.list_present(self.visited,temp)
            if check1 == False and check2 == False:
                self.add_to_priority_queue(temp)

#Function that checks and moves the zero to the left if possible
    def move_left(self,current):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (col>0):
            temp.value[row,col-1] = current.value[row,col]
            temp.value[row,col] = current.value[row,col-1]
            temp.heurestic = self.heurestic_value(temp)
            check1 = self.list_present(self.priority_queue,temp)
            check2 = self.list_present(self.visited,temp)
            if check1 == False and check2 == False:
                self.add_to_priority_queue(temp)

#Function that checks and moves the zero up if possible
    def move_up(self,current):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (row>0):
            temp.value[row-1,col] = current.value[row,col]
            temp.value[row,col] = current.value[row-1,col]
            temp.heurestic = self.heurestic_value(temp)
            check1 = self.list_present(self.priority_queue,temp)
            check2 = self.list_present(self.visited,temp)
            if check1 == False and check2 == False:
                self.add_to_priority_queue(temp)

#Function that checks and moves the zero down if possible
    def move_down(self,current):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (row<2):
            temp.value[row+1,col] = current.value[row,col]
            temp.value[row,col] = current.value[row+1,col]
            temp.heurestic = self.heurestic_value(temp)
            check1 = self.list_present(self.priority_queue,temp)
            check2 = self.list_present(self.visited,temp)
            if check1 == False and check2 == False:
                self.add_to_priority_queue(temp)
    
#Function to trace the path back from the parent node to the goal node  
    def path_traversed(self,current):
        while((current.value==self.start.value).all()==False):
            self.path.append(current)
            current = current.parent
        self.path.append(self.start)
        self.path.reverse()
        print("Path taken to reach from Initial State to Goal State:")
        for i in self.path:
            print(i.value)
            print()
        print("Number of moves = ",len(self.path)-1)

#Main part of the Greedy Best Search Algorithm
#Every next node is the node with the smallest value of heurestic function in the priority queue
#In other words every next state is the first element of the priority queue
    def GBFS(self):
        current = State(None,None)
        if self.priority_queue==[]:
            current = deepcopy(self.start)
            self.priority_queue.append(current)
        while((current.value==self.goal).all()==False):
            self.move_down(current)
            self.move_left(current)
            self.move_right(current)
            self.move_up(current)
            self.priority_queue.remove(current)
            self.visited.append(current)
            current = self.priority_queue[0]
        self.path_traversed(current)
            
I = np.array([[7,2,4],[5,0,6],[8,3,1]]) #Initial State
G = np.array([[0,1,2],[3,4,5],[6,7,8]]) #Goal State  
graph1 = Greedy_Best_Search(I,G)
