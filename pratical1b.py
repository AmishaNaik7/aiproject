from collections import deque


# Generate possible next states
def generate_successors(state):
    successors = []

    stacks = [list(stack) for stack in state]

    for i in range(len(stacks)):

        if len(stacks[i]) == 0:
            continue

        # Top block
        block = stacks[i][-1]

        for j in range(len(stacks)):

            if i == j:
                continue

            # Copy current state
            new_stacks = [stack[:] for stack in stacks]

            # Remove block from source stack
            new_stacks[i].pop()

            # Put block on destination stack
            new_stacks[j].append(block)

            new_state = tuple(tuple(stack) for stack in new_stacks)

            action = "Move " + block + \
                     " from Stack " + str(i + 1) + \
                     " to Stack " + str(j + 1)

            successors.append((new_state, action))

    return successors


# BFS
def bfs(initial_state, goal_state):

    queue = deque()

    queue.append((initial_state, []))

    visited = set()
    visited.add(initial_state)

    while queue:

        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for next_state, action in generate_successors(current_state):

            if next_state not in visited:

                visited.add(next_state)

                new_path = path + [(action, next_state)]

                queue.append((next_state, new_path))

    return None


# Display state
def display_state(state):

    for i, stack in enumerate(state):
        print("Stack", i + 1, ":", list(stack))


# -------------------------------
# MAIN PROGRAM
# -------------------------------

print("================================")
print("      BLOCKS WORLD USING BFS")
print("================================")

# Number of stacks
n = int(input("\nEnter number of stacks: "))

# Initial state
print("\nEnter Initial State")
print("Enter blocks from bottom to top.")
print("Example: A B C")

initial_stacks = []

for i in range(n):

    data = input("Enter Stack " + str(i + 1) + ": ")

    if data == "0":
        initial_stacks.append(())
    else:
        blocks = data.upper().split()
        initial_stacks.append(tuple(blocks))

initial_state = tuple(initial_stacks)


# Goal state
print("\nEnter Goal State")
print("Enter blocks from bottom to top.")
print("Example: C B A")

goal_stacks = []

for i in range(n):

    data = input("Enter Stack " + str(i + 1) + ": ")

    if data == "0":
        goal_stacks.append(())
    else:
        blocks = data.upper().split()
        goal_stacks.append(tuple(blocks))

goal_state = tuple(goal_stacks)


# Display states
print("\n---------- INITIAL STATE ----------")
display_state(initial_state)

print("\n------------ GOAL STATE ------------")
display_state(goal_state)


# BFS search
print("\nSearching using BFS...")

solution = bfs(initial_state, goal_state)


# Display solution
if solution is not None:

    print("\n========== SOLUTION FOUND ==========")
    print("Number of steps:", len(solution))

    for step, (action, state) in enumerate(solution, 1):

        print("\nStep", step)
        print("Action:", action)

        display_state(state)

else:

    print("\nNo solution found.")