import ai_player.py

CUTOFF = "cutoff"
FAILURE = "failure"

class Depth_Limited_Player:
    def __init__(self, thing):
        self.thing_ = thing
        AIPlayer.__init__(self, thing)

    # def search_moves():
    #     recursive_DLS(node, problem, limit)
    #
    # def recursive_DLS(node, problem, limit):
    #     if robot reached target:
    #         return solution
    #     elif limit == 0
    #         return CUTOFF
    #     else
    #         cutoff_occurred = False
    #         for each robot:
    #             for each move direction:
    #                 child = child_node(problem, node, action)
    #                 result = recursive_DLS(node, problem, limit-1)
    #                 if result == CUTOFF:
    #                     cutoff_occurred = True
    #                 elif result != FAILURE:
    #                     return result
    #         if cutoff_occurred:
    #             return CUTOFF
    #         else return FAILURE
