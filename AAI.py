from ai_player import *
import copy
import random

from stack import Stack
from node import Node

class Actual_AI_Player:
    def __init__(self):
        AIPlayer.__init__(self, None, None, None)

    def search(self, board, target, robots, limit):
        finalNode = self.graph_search(board, target, robots)

    def find_min_index(self, frontier):
        min_index = 0
        min_cost = float("inf")
        for i in range(len(frontier)):
            if (frontier[i].get_cost() < min_cost):
                min_index = i
                min_cost = frontier[i].get_cost()
        return min_index

    def graph_search(self, board, target, robots):
        frontier = []
        expanded = []
        initialState = copy.deepcopy(robots)
        initialNode = Node(initialState, 0, 0, 0, 0)
        frontier.append(initialNode)

        while True:
            if (len(frontier) == 0):
                return FAILURE

            # remove node at top of priority queue
            min_index = self.find_min_index(frontier)
            currentNode = Node.copyNode(frontier[min_index])
            del frontier[min_index]
            expanded.append(Node.copyNode(currentNode))

            for r in currentNode.robots_: # goal test
                if (target.color_ == r.color_ and target.x_ == r.x_ and target.y_ == r.y_):
                    return currentNode

            for i in range(len(currentNode.robots_)): # for each robot
                direction = ["NORTH", "SOUTH", "EAST", "WEST"]
                for j in range (len(direction)): # for each direction
                    if (currentNode.robots_[i].move_possible(board, robots, direction[j])): # check if valid move
                        newNode = Node.copyNode(currentNode)
                        unique_node = True
                        newNode.robots_[i] = newNode.robots_[i].move(board, robots, direction[j])

                        # calculate cost of newNode
                        newNode.g_ = newNode.g_ + 1;
                        h = 0;
                        # for r in range(len(newNode.robots_)):
                        #     if (newNode.robots_[r].color_ == target.color_):
                        #         h = abs(newNode.robots_[r].x_ - target.x_) + abs(newNode.robots_[r].y_ - target.y_)
                        newNode.h_ = h;

                        print("Moving robot " + str(i) + " " + direction[j] + " at depth " + str(newNode.g_))
                        newNode.move_tuple_ = (i, direction[j])
                        newNode.father_ = currentNode

                        for m in range (len(frontier)): # check if newNode is already in frontier
                            if (Node.compareState(frontier[m],newNode)==True):
                                unique_node = False
                                break
                        for n in range(len(expanded)): # check if newNode has already been expanded
                            if (Node.compareState(expanded[n],newNode)==True):
                                unique_node = False
                                break
                        if(unique_node): frontier.append(Node.copyNode(newNode))
