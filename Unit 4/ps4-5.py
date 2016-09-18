# Stochastic Motion
# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']  # Use these when creating your policy grid.


# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    failure_prob = (1.0 - success_prob) / 2.0  # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True   # check if grids of policy and value still change the value of its cells.

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:     # initialize the value of goal to 0
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            # compute stochastic motion here
                            sa1 = (a-1) % 4
                            sa1_cost = 0
                            x3 = x + delta[sa1][0]
                            y3 = y + delta[sa1][1]
                            if x3 >= 0 and x3 < len(grid) and y3 >= 0 and y3 < len(grid[0]) and grid[x3][y3] == 0:
                                sa1_cost = failure_prob * value[x3][y3]
                            else:
                                sa1_cost = failure_prob * collision_cost

                            sa2 = (a+1) % 4
                            sa2_cost = 0
                            x4 = x + delta[sa2][0]
                            y4 = y + delta[sa2][1]
                            if x4 >= 0 and x4 < len(grid) and y4 >= 0 and y4 < len(grid[0]) and grid[x4][y4] == 0:
                                sa2_cost = failure_prob * value[x4][y4]
                            else:
                                sa2_cost = failure_prob * collision_cost

                            # compute total cost of stochastic motion
                            v2 = value[x2][y2] * success_prob + sa1_cost + sa2_cost + cost_step

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]


    return value, policy


# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0]) - 1]  # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

value, policy = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print row
for row in policy:
    print row

    # Expected outputs:
    #
    # [57.9029, 40.2784, 26.0665,  0.0000]
    # [47.0547, 36.5722, 29.9937, 27.2698]
    # [53.1715, 42.0228, 37.7755, 45.0916]
    # [77.5858, 100.00, 100.00, 73.5458]
    #
    # ['>', 'v', 'v', '*']
    # ['>', '>', '^', '<']
    # ['>', '^', '^', '<']
    # ['^', ' ', ' ', '^']