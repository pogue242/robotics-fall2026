"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct, free


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]
    
    front = deque([ctx.start])
    p = {ctx.start: None}
    
    while front:
        current = front.popleft()
        if current == ctx.goal:
            return reconstruct(p, current)
        for neighbor in ctx.expand(current, len(front) + 1):
            if neighbor not in p:
                p[neighbor] = current
                front.append(neighbor)
                
    return []

def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    
    if ctx.start == ctx.goal:
        return [ctx.start]
    
    front = [ctx.start]
    p = {ctx.start: None}
    
    while front:
        current = front.pop()
        if current == ctx.goal:
            return reconstruct(p, current)
        neighbors = ctx.expand(current, len(front) + 1)
        for neighbor in reversed(neighbors):
            if neighbor not in p:
                p[neighbor] = current
                front.append(neighbor)
                
    return []

def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    
    if ctx.start == ctx.goal:
        return [ctx.start]
    
    free_cells = sum(cell == 0 for row in ctx.grid for cell in row)
    
    for limit in range(free_cells):
        front = [(ctx.start, [ctx.start], 0)]
        cutoff = False
        while front:
            current, path, depth = front.pop()
            if current == ctx.goal:
                return path
            neighbors = [neighbor for neighbor in ctx.expand(current, len(front) + 1) if neighbor not in path]
            if depth < limit:
                for neighbor in reversed(neighbors):
                    front.append((neighbor, path + [neighbor], depth + 1))
            elif neighbors:
                cutoff = True
        if not cutoff:
            return []
        
    return []

def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]
    cost = {ctx.start: 0}
    p = {ctx.start: None}
    front = [(ctx.heuristic(ctx.start), 0, ctx.start)]
    while front:
        _, current_cost, current = heappop(front)
        if current_cost != cost.get(current):
            continue
        if current == ctx.goal:
            return reconstruct(p, current)
        for neighbor in ctx.expand(current, len(front) + 1):
            curr_cost = current_cost + 1
            if curr_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = curr_cost
                p[neighbor] = current
                priority = curr_cost + ctx.heuristic(neighbor)
                heappush(front, (priority, curr_cost, neighbor))
    return []