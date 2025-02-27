from MinBinaryHeap import MinBinaryHeap
import time
from ComplementaryFunctions import generateStates, manhattanDistance, determineActions, successorState, checkAdjacent, find_nearest_unblocked, reconstruct_path
from State import State

def computePath(open_list, closed_list, goal, expanded, counter, states):
    while goal.g > open_list.peek().f:
        current = open_list.pop() # pop the min f valued state from the heap
        closed_list.add(current) # add the current state to the closed state since it is going to be expanded
        
        expanded.append((current.x, current.y)) 
        
        for action in determineActions(current, states, closed_list):
            successor = successorState(current, action, states)
            
            if successor.search < counter:
                successor.g = float('inf')
                successor.search = counter
                
            if successor.g > current.g + 1:
                successor.g = current.g + 1
                successor.pointer = current
                
                if open_list.contains(successor): # if successor in open list, remove it 
                    open_list.remove(successor)
                
                successor.update() # update f value
                open_list.insert(successor)
                
        if open_list.isEmpty():
            break
        
def repeatedForwardMain(grid_path, start, goal, larger_g = True):
    states = generateStates(grid_path, larger_g)
    
    start_state = states[start[0]][start[1]]
    goal_state = states[goal[0]][goal[1]]

    # Check if start is blocked
    if start_state.isBlocked:
        print(f"Start state {start} is blocked. Searching for nearest unblocked state...")
        start_state = find_nearest_unblocked(start, states)
        if not start_state:
            print("No unblocked state found near start. Terminating.")
            return None, None, None
    
    # Check if goal is blocked
    if goal_state.isBlocked:
        print(f"Goal state {goal} is blocked. Searching for nearest unblocked state...")
        goal_state = find_nearest_unblocked(goal, states)
        if not goal_state:
            print("No unblocked state found near goal. Terminating.")
            return None, None, None
        
    if start_state is None or goal_state is None:
        print("No valid path exists in this grid. Terminating.")
        return None, None, None
    
    counter = 0
    path = []
    expanded = []
    
    checkAdjacent(start_state, states)
    path.append((start_state.x, start_state.y))
    
    for rows in states:
        for state in rows:
            state.h = manhattanDistance(state, goal_state)
        
    start_time = time.time()
    while start_state != goal_state:
        counter += 1
        
        start_state.g = 0
        start_state.search = counter
        goal_state.g = float('inf')
        goal_state.search = counter
        
        open_list = MinBinaryHeap()
        closed_list = set()
        
        start_state.update()
        open_list.insert(start_state)
        
        computePath(open_list, closed_list, goal_state, expanded, counter, states)
        
        if open_list.isEmpty():
            return path, expanded, time.time() - start_time
                
        while start_state != goal_state:
            current = goal_state
            
            while (current.pointer is not None) and (current != start_state):
                if current.pointer == start_state:
                    break
                current = current.pointer
                
            if current.isObserved is False:
                start_state = current
                path.append((start_state.x, start_state.y))
                checkAdjacent(start_state, states)
            else: 
                break
            
    expanded.append((goal_state.x, goal_state.y))
    print(path)
    shortest_path = reconstruct_path(path)
    end_time = time.time()
        
    return shortest_path, expanded, end_time - start_time


    
    
    
                
            