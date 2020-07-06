import numpy as np
from queue import PriorityQueue
import random
import time

class Tree:
    class Node:
        def __init__(self, state, parent=None):
            self.state = state
            self.parent = parent
            self.weight = Tree.Node.calcManhattan(self.state)
            self.edges = [None, None, None, None]
            if not(parent is None):
                self.level = parent.level + 1
            else:
                self.level = 0

        def __hash__(self):
            return hash(np.array_str(self.state.flatten()))

        def __lt__(self,other):
            return self.weight < other.weight
        
        def __eq__(self,other):
            return self.weight == other.weight

        def __gt__(self,other):
            return self.weight > other.weight

        def calcManhattan(state):
            goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
            suma = 0
            for i in range(0,3):
                for j in range(0,3):
                    g = goal[i][j]
                    s = np.where(state == g)
                    suma = suma + abs(i - s[0][0]) + abs(j - s[1][0])
            #print(suma)
            return suma

    def __init__(self, initState, maxNodes=100000):
        self.initState = initState
        self.goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.initNode = Tree.Node(state=self.initState)
        self.goalNode = None
        self.i = 0
        self.maxNodes = maxNodes

    def solveAStar(self):
        self.goalNode = None
        visitedStates = set()
        nodes = PriorityQueue(100000)
        nodes.put(self.initNode)
        t1 = time.process_time()
        #nodes = [self.initNode]
        visitedStates.add(np.array_str(self.initNode.state.flatten()))
        i = 1
        k = 0
        while(k <= self.maxNodes):
            k += 1
            currNode = nodes.get()
            #currNode = nodes.pop(0)
            
            z = np.where(currNode.state == 0)
            zero = (z[0][0],z[1][0])

            if not(zero[0]-1 < 0):
                #print("Up")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]-1][zero[1]]
                newState[zero[0]-1][zero[1]] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                    currNode.edges[0] = newNode
                    nodes.put(newNode)
                    #nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break

            if not(zero[1]+1 > 2):
                #print("rigth")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]][zero[1]+1]
                newState[zero[0]][zero[1]+1] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                    currNode.edges[1] = newNode
                    nodes.put(newNode)
                    #nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break

            if not(zero[0]+1 > 2):
                #print("down")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]+1][zero[1]]
                newState[zero[0]+1][zero[1]] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                    currNode.edges[2] = newNode
                    nodes.put(newNode)
                    #nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break

            if not(zero[1]-1 < 0):
                #print("left")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]][zero[1]-1]
                newState[zero[0]][zero[1]-1] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state= np.copy(newState),parent=currNode)
                    currNode.edges[3] = newNode
                    nodes.put(newNode)
                    #nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break
            #print()
        self.i = i
                
    def solveBFS(self):
        self.goalNode = None
        visitedStates = set()
        t1 = time.process_time()
        nodes = [self.initNode]
        visitedStates.add(np.array_str(self.initNode.state.flatten()))
        i = 1
        k = 0
        while(k <= self.maxNodes):
            k += 1
            currNode = nodes.pop(0)
            #print(currNode.level)
            z = np.where(currNode.state == 0)
            zero = (z[0][0],z[1][0])

            if not(zero[0]-1 < 0):
                #print("Up")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]-1][zero[1]]
                newState[zero[0]-1][zero[1]] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                    currNode.edges[0] = newNode
                    nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break

            if not(zero[1]+1 > 2):
                #print("rigth")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]][zero[1]+1]
                newState[zero[0]][zero[1]+1] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                    currNode.edges[1] = newNode
                    nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break

            if not(zero[0]+1 > 2):
                #print("down")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]+1][zero[1]]
                newState[zero[0]+1][zero[1]] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                    currNode.edges[2] = newNode
                    nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break

            if not(zero[1]-1 < 0):
                #print("left")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]][zero[1]-1]
                newState[zero[0]][zero[1]-1] = 0
                #print(newState)
                if not(np.array_str(newState.flatten()) in visitedStates):
                    visitedStates.add(np.array_str(newState.flatten()))
                    newNode = Tree.Node(state= np.copy(newState),parent=currNode)
                    currNode.edges[3] = newNode
                    nodes.append(newNode)
                    i += 1
                    if(newNode.weight == 0):
                        self.goalNode = newNode
                        break
            #print()
        self.i = i

    def solveDLS(self, limit):
        self.goalNode = None
        t1 = time.process_time()
        nodes = [self.initNode]
        i = 1
        maxn = 30
        while(len(nodes)>0):
            currNode = nodes.pop()

            if(currNode.level > limit):
                continue
            
            z = np.where(currNode.state == 0)
            zero = (z[0][0],z[1][0])

            if not(zero[0]-1 < 0):
                #print("Up")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]-1][zero[1]]
                newState[zero[0]-1][zero[1]] = 0
                #print(newState)
                newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                currNode.edges[0] = newNode
                nodes.append(newNode)
                i += 1
                if(newNode.weight == 0):
                    self.goalNode = newNode
                    break

            if not(zero[1]+1 > 2):
                #print("rigth")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]][zero[1]+1]
                newState[zero[0]][zero[1]+1] = 0
                #print(newState)
                newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                currNode.edges[1] = newNode
                nodes.append(newNode)
                i += 1
                if(newNode.weight == 0):
                    self.goalNode = newNode
                    break

            if not(zero[0]+1 > 2):
                #print("down")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]+1][zero[1]]
                newState[zero[0]+1][zero[1]] = 0
                #print(newState)
                newNode = Tree.Node(state=np.copy(newState),parent=currNode)
                currNode.edges[2] = newNode
                nodes.append(newNode)
                i += 1
                if(newNode.weight == 0):
                    self.goalNode = newNode
                    break

            if not(zero[1]-1 < 0):
                #print("left")
                newState = np.copy(currNode.state)
                newState[zero[0]][zero[1]] = newState[zero[0]][zero[1]-1]
                newState[zero[0]][zero[1]-1] = 0
                #print(newState)
                newNode = Tree.Node(state= np.copy(newState),parent=currNode)
                currNode.edges[3] = newNode
                nodes.append(newNode)
                i += 1
                if(newNode.weight == 0):
                    self.goalNode = newNode
                    break
        self.i = i
        return [i, self.goalNode]