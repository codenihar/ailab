class State:
    def __init__(self, monkey_loc, monkey_on_box, box_loc, monkey_has_banana):
        self.monkey_loc = monkey_loc
        self.monkey_on_box = monkey_on_box
        self.box_loc = box_loc
        self.monkey_has_banana = monkey_has_banana

    def __str__(self):
        return f"Monkey:{self.monkey_loc}, on box:{self.monkey_on_box}, Box:{self.box_loc}, Has Banana:{self.monkey_has_banana}"

    def grasp(state):
        state.monkey_has_banana = True
        return state

    def climb(state):
        state.monkey_on_box = True
        return state

    def drag(state, P1, P2):
        state.box_loc = P2
        return state

    def walk(state, P1, P2):
        state.monkey_loc = P2
        return state

    def can_get(state):
        return state.monkey_has_banana

def solve():
    ins = State("middle", False, "middle", False)
    state1 = ins.walk("left", "right")
    print(f"Step 1: {state1}")
    state2 = state1.drag("middle", "right")
    print(f"Step 2: {state2}")
    state3 = state2.climb()
    print(f"Step 3: {state3}")
    state4 = state3.grasp()
    print(f"Step 4: {state4}")
    
    if state4.can_get():
        print("Goal reached: Monkey has the banana!")
    else:
        print("Goal not reached")

solve()
