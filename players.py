import numpy as np
import time
import random
from queue import PriorityQueue
from tree import Tree

def main():
    #T = Tree(np.array([[5,2,8],[4,1,7],[0,3,6]]))
    maxDepth = 10
    maxIterations = 10
    T = Tree(np.array([[4,1,0],[2,6,3],[7,5,8]]))

    t1 = time.process_time()
    T.solveAStar()
    t2 = time.process_time()
    print("A*")
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
    #l = list(range(9))
    #random.shuffle(l)
    #print(l)
    #T = Tree(np.array([[l[0],l[1],l[2]],[l[3],l[4],l[5]],[l[6],l[7],l[8]]]))

if __name__ == "__main__":
    main()