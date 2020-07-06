import numpy as np
import time
import random
from queue import PriorityQueue
from tree import Tree

def main():
    maxDepth = 14
    maxIterations = 14
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    l = list(range(9))
    random.shuffle(l)
    #initState = np.array([[l[0],l[1],l[2]],[l[3],l[4],l[5]],[l[6],l[7],l[8]]])
    initState = np.array([[4,1,0],[2,6,3],[7,5,8]])
    #initState = np.array([[5,2,8],[4,1,7],[0,3,6]])
    #initState = np.array([[1,2,3],[4,5,6],[8,7,0]])

    print("Initial State:\n", initState)

    flatState = initState.flatten()
    inv_count = 0
    for i in range(0,8):
        for j in range(i+1,9):
            if flatState[i] and flatState[j] and flatState[i] > flatState[j]:
                inv_count += 1; 
    if inv_count%2 == 1:
        print("Not solvable")
        return 0
    T = Tree(initState, maxNodes=100000)

    t1 = time.process_time()
    T.solveAStar()
    t2 = time.process_time()
    print("====================================")
    print("A* - Manhattan")
    if T.goalNode is None:
        print("Did not find goal node")
    else:
        print("found goal node: \n",T.goalNode.state, " \nLevel: ",T.goalNode.level)
    print("Total:",T.i,"Created nodes")
    print("Took", t2-t1,"seconds to create the tree")

    t1 = time.process_time()
    T.solveAStar(heur="T")
    t2 = time.process_time()
    print("====================================")
    print("A* - Tiles")
    if T.goalNode is None:
        print("Did not find goal node")
    else:
        print("found goal node: \n",T.goalNode.state, " \nLevel: ",T.goalNode.level)
    print("Total:",T.i,"Created nodes")
    print("Took", t2-t1,"seconds to create the tree")

    t1 = time.process_time()
    T.solveBFS()
    t2 = time.process_time()
    print("====================================")
    print("BFS")
    if T.goalNode is None:
        print("Did not find goal node")
    else:
        print("found goal node: \n",T.goalNode.state, " \nLevel: ",T.goalNode.level)
    print("Total:",T.i,"Created nodes")
    print("Took", t2-t1,"seconds to create the tree")

    t1 = time.process_time()
    ans = T.solveDLS(maxDepth)
    t2 = time.process_time()
    print("====================================")
    print("DLS")
    if T.goalNode is None:
        print("Did not find goal node")
    else:
        print("found goal node: \n",T.goalNode.state, " \nLevel: ",T.goalNode.level)
    print("Total:",T.i,"Created nodes")
    print("Took", t2-t1,"seconds to create the tree")

    totali = 0
    maxIndex = 0
    t1 = time.process_time()
    for index in range(maxIterations):
        ans = T.solveDLS(index)
        maxIndex = index
        totali += ans[0]
        if(T.goalNode is not None):
            break
    t2 = time.process_time()
    print("====================================")
    print("IDDFS")
    if T.goalNode is None:
        print("Did not find goal node")
    else:
        print("found goal node: \n",T.goalNode.state, " \nLevel: ",T.goalNode.level)
    print("Total: ",totali,"Created nodes")
    print("MaxLevel: ",maxIndex)
    print("Took", t2-t1,"seconds to create the tree")
    

if __name__ == "__main__":
    main()