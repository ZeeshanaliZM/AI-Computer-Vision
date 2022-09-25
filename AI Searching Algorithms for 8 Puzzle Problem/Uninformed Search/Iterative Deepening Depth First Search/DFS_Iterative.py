#Solving 8 puzzle problem using Iterative Deepening Depth First Search.
#The advantage of this is that since the depth increases after each iteration, it will give us the optimal solution.
#Disadvnatage is that it repeats the entire process again if goal node not found
import numpy as np
from copy import deepcopy

#Declare each state as having a value and the link to each parent state
class State:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent

#Declare the class to intialize the depth first search tree
class Depth_Iterative_Search:
    def __init__(self,initial,goal):
        self.start = State(initial,None)
        self.goal = goal
        self.max_depth = -1
        self.path = []
        self.visited = []
        self.stack = []
        self.DFS_Iterative()

#This function is used to ensure to repeatitive states occur in the stack. 
#No need for visited list check since we only add elements in depthwise order first and their are checked alltogheter at the end
    def list_present(self,list_check,current):
        for i in list_check:
            if((current.value==i.value).all()==True):
                return True
        else:
            return False

#To locate the position of the zeros in each state
    def find_zeros(self,current):
        return np.where(current.value==0)

#Function that checks and moves the zero to the right if possible
    def move_right(self,current,depth):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (col<2):
            temp.value[row,col+1] = current.value[row,col]
            temp.value[row,col] = current.value[row,col+1]
            check1 = self.list_present(self.stack,temp)
            if check1 == False:
                self.stack.append(temp)
                self.max_depth_check(temp,depth) #Calling the max depth checking function

#Function that checks and moves the zero to the left if possible
    def move_left(self,current,depth):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (col>0):
            temp.value[row,col-1] = current.value[row,col]
            temp.value[row,col] = current.value[row,col-1]
            check1 = self.list_present(self.stack,temp)
            if check1 == False:
                self.stack.append(temp)
                self.max_depth_check(temp,depth) #Calling the max depth checking function

#Function that checks and moves the zero up if possible
    def move_up(self,current,depth):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (row>0):
            temp.value[row-1,col] = current.value[row,col]
            temp.value[row,col] = current.value[row-1,col]
            check1 = self.list_present(self.stack,temp)
            if check1 == False:
                self.stack.append(temp)
                self.max_depth_check(temp,depth) #Calling the max depth checking function

#Function that checks and moves the zero down if possible
    def move_down(self,current,depth):
        row = self.find_zeros(current)[0]
        col = self.find_zeros(current)[1]
        temp = State(current.value.copy(),current)
        if (row<2):
            temp.value[row+1,col] = current.value[row,col]
            temp.value[row,col] = current.value[row+1,col]
            check1 = self.list_present(self.stack,temp)
            if check1 == False:
                self.stack.append(temp)
                self.max_depth_check(temp,depth) #Calling the max depth checking function

#This function is used to check if the maximum depth is equal to the current depth.
#Each state has parent states ad child states.
#States occuring from the same parent are at the same level.
#In the function we only add the elements to the stack depthwise until it reaches the maximum allocated depth.
#This function is called recursively until the current depth == Maximum depth. Once equal it exits from the current function and proceeds to the next child of the parent.
#It needs to be called in the moving functions and the moving function need to called in it to be performed recusively.
    def max_depth_check(self,current,depth):
        if depth == self.max_depth:
            return
        else:
            depth +=1
            self.move_left(current,depth) #Calling the moving functions
            self.move_up(current,depth) #Calling the moving functions
            self.move_right(current,depth) #Calling the moving functions
            self.move_down(current,depth) #Calling the moving functions
            return

#This function is used to restart the search once it has check all the elements abouve a certain depth.
#Once all the elements above a certain depth are checked, If goal is not found it restarts the checking and increases the maximum posssible depth by 1.
    def restart_search(self):
        if self.stack == []:
            current = deepcopy(self.start)
            self.stack.append(current)
            self.max_depth +=1
            self.visited.clear()
            return current

#The main loop where the stack that is filled depthwise is checked.
#While chcking if the goal is found, the loop stops and the path back to the initial state is traced.
#If the goal is not found, when the stack becomes empty, the search is restarted and the maximum depth is increased by 1.
    def DFS_Iterative(self):
        current_depth = 0
        current = State(None,None)
        while((current.value==self.goal).all()==False):
            if self.stack == []:
                current = self.restart_search()
                self.max_depth_check(current,current_depth)
            #print(current.value)
            #print()
            self.visited.append(current)
            self.stack.remove(current)
            if self.stack!=[]:
                current = self.stack[0]
        self.path_traversed(current)

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
            
I = np.array([[1,8,2],[0,4,3],[7,6,5]]) #Initial State
G = np.array([[1,2,3],[4,5,6],[7,8,0]]) #Goal State
tree1 = Depth_Iterative_Search(I,G)
