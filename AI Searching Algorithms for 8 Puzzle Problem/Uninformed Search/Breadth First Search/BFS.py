#Algorithm to search for a solution to 8 puzzle problem using Breadth First Search
import numpy as np
from copy import deepcopy
#The resulting state obtained from each movement is treated as a node and has two data members:
#1. The value of the state
#2. The parent of the state to keep track once we find the goal state

class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent

#Define the class of the tree
class Breadth_First_Search:
    def __init__(self,initial,goal):
        self.start = Node(initial,None)
        self.goal = goal
        self.queue = []
        self.visited = []
        self.path = []
        self.BFS()

#Define a function to look for the zeros in each state. 
    def find_zero(self,current):
        pos = np.where(current.value == 0)
        return pos

#check if the state is pesent in the queue or visited list.
#If the state is present in either, dont add the state to the queue.
    def list_present(self,list_check,current):
        for i in list_check:
            if((current.value==i.value).all()==True):
                return True
        else:
            return False

#define the movements possible for the 0.
#It can move right if column<2
    def move_right(self,current):
        row = self.find_zero(current)[0]
        col = self.find_zero(current)[1]
        temp = Node(current.value.copy(),current)
        if(col<2):
            temp.value[row,col+1] = current.value[row,col]
            temp.value[row,col] = current.value[row,col+1]
            check1 = self.list_present(self.queue,temp)
            check2 = self.list_present(self.visited,temp)
            #print(check1)
            #print(check2)
            if(check1 == False and check2 == False):
                self.queue.append(temp)
        #print(current.value)
        #print(temp.value)

#It can move dwon if row<2
    def move_down(self,current):
        row = self.find_zero(current)[0]
        col = self.find_zero(current)[1]
        temp = Node(current.value.copy(),current)
        if(row<2):
            temp.value[row+1,col] = current.value[row,col]
            temp.value[row,col] = current.value[row+1,col]
            check1 = self.list_present(self.queue,temp)
            check2 = self.list_present(self.visited,temp)
            #print(check1)
            #print(check2)
            if(check1 == False and check2 == False):
                self.queue.append(temp)
        #print(current.value)
        #print(temp.value)

#It can move left if column>0
    def move_left(self,current):
        row = self.find_zero(current)[0]
        col = self.find_zero(current)[1]
        temp = Node(current.value.copy(),current)
        if(col>0):
            temp.value[row,col-1] = current.value[row,col]
            temp.value[row,col] = current.value[row,col-1]
            check1 = self.list_present(self.queue,temp)
            check2 = self.list_present(self.visited,temp)
            #print(check1)
            #print(check2)
            if(check1 == False and check2 == False):
                self.queue.append(temp)
        #print(current.value)
        #print(temp.value)

#It can move up if rown>0
    def move_up(self,current):
        row = self.find_zero(current)[0]
        col = self.find_zero(current)[1]
        temp = Node(current.value.copy(),current)
        if(row>0):
            temp.value[row-1,col] = current.value[row,col]
            temp.value[row,col] = current.value[row-1,col]
            check1 = self.list_present(self.queue,temp)
            check2 = self.list_present(self.visited,temp)
            #print(check1)
            #print(check2)
            if(check1 == False and check2 == False):
                self.queue.append(temp)
        #print(current.value)
        #print(temp.value)

#Define the function to print the actual path and moves once it finds the goal state    
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

#The main part of the searching algorithm where we look for the goal state.
#The movement is anticlockwise starting from left
    def BFS(self):
        count = 1 #To check for the number of states that have been searched 
        current = deepcopy(self.start)
        self.queue.append(current)
        while((current.value==self.goal).all()==False):
            self.move_left(current)
            self.move_down(current)
            self.move_right(current)
            self.move_up(current)
            self.visited.append(current)
            self.queue.remove(current)
            current = self.queue[0]
            #count+=1
            #print(current.value)
            #print(count)
            #print()
        self.path_traversed(current)
        
I = np.array([[1,8,2],[0,4,3],[7,6,5]])
G = np.array([[1,2,3],[4,5,6],[7,8,0]])
tree1 = Breadth_First_Search(I,G)
