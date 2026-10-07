# Goal Stack Planning - Blocks World

def goal_stack_planning(initial_state, goal_state):
    state = set(initial_state)
    stack = []
    plan = []

    # Push goals onto stack
    for goal in reversed(goal_state):
        stack.append(("GOAL", goal))

    while stack:

        item_type, item = stack.pop()

        # If it is a goal
        if item_type == "GOAL":

            if item in state:
                continue

            # ON(A,B)
            if item.startswith("ON("):
                a, b = item[3:-1].split(",")

                # Preconditions for STACK(A,B)
                preconditions = [
                    f"HOLDING({a})",
                    f"CLEAR({b})"
                ]

                stack.append(("ACTION", f"STACK({a},{b})"))

                for pre in reversed(preconditions):
                    stack.append(("GOAL", pre))

            # HOLDING(A)
            elif item.startswith("HOLDING("):
                a = item[8:-1]

                stack.append(("ACTION", f"PICKUP({a})"))

                stack.append(("GOAL", f"ONTABLE({a})"))
                stack.append(("GOAL", f"CLEAR({a})"))
                stack.append(("GOAL", "ARMEMPTY"))

            # CLEAR(A)
            elif item.startswith("CLEAR("):
                a = item[6:-1]

                # Assume block is clear if nothing is ON it
                if not any(
                    x.startswith("ON(") and x.endswith("," + a + ")")
                    for x in state
                ):
                    state.add(f"CLEAR({a})")

            # ONTABLE(A)
            elif item.startswith("ONTABLE("):
                a = item[8:-1]
                state.add(f"ONTABLE({a})")

            elif item == "ARMEMPTY":
                state.add("ARMEMPTY")

        # If it is an action
        elif item_type == "ACTION":

            action = item

            if action.startswith("PICKUP("):
                a = action[7:-1]

                if (
                    f"ONTABLE({a})" in state
                    and f"CLEAR({a})" in state
                    and "ARMEMPTY" in state
                ):
                    state.remove(f"ONTABLE({a})")
                    state.remove(f"CLEAR({a})")
                    state.remove("ARMEMPTY")

                    state.add(f"HOLDING({a})")
                    plan.append(action)

            elif action.startswith("STACK("):
                a, b = action[6:-1].split(",")

                if (
                    f"HOLDING({a})" in state
                    and f"CLEAR({b})" in state
                ):
                    state.remove(f"HOLDING({a})")
                    state.remove(f"CLEAR({b})")

                    state.add(f"ON({a},{b})")
                    state.add(f"CLEAR({a})")
                    state.add("ARMEMPTY")

                    plan.append(action)

    return plan, state


# Initial state
initial_state = {
    "ONTABLE(A)",
    "ONTABLE(B)",
    "ONTABLE(C)",
    "CLEAR(A)",
    "CLEAR(B)",
    "CLEAR(C)",
    "ARMEMPTY"
}

# Goal state
goal_state = [
    "ON(B,C)",
    "ON(A,B)"
]

# Solve the problem
plan, final_state = goal_stack_planning(initial_state, goal_state)

print("Goal Stack Planning")
print("--------------------")

print("\nInitial State:")
for item in initial_state:
    print(item)

print("\nPlan:")
for i, action in enumerate(plan, 1):
    print(i, ".", action)

print("\nFinal State:")
for item in final_state:
    print(item)