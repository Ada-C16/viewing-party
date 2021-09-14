from gameoflife import width, height, stage, print_stage, count_neighbors

def init_stage(stage):
    for v_pos in range(0, height):
        for h_pos in range(0, width):
            if h_pos == 1:
                stage[v_pos][h_pos] = True
        else:
            stage[v_pos][h_pos] = False

# Generation Rules:
# 1. Any live cell with < 2 neighbors dies
# 2. Any live cell with 2-3 neighbors lives
# 3. Any live cell with > 3 neighbors dies
# 4. Any dead cell with 3 neighbors comes alive

def one_generation(stage):
    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[v_pos])):
            neighbors = count_neighbors(stage, v_pos, h_pos)
            if not stage[v_pos][h_pos] and neighbors == 3:
                stage[v_pos][h_pos] = True
            elif stage[v_pos][h_pos] and neighbors < 2:
                stage[v_pos][h_pos] = False
            elif stage[v_pos][h_pos] and (neighbors == 2 or neighbors == 3):
                stage[v_pos][h_pos] = True
            elif stage[v_pos][h_pos] and neighbors > 3:
                stage[v_pos][h_pos] = False
                

init_stage(stage)
print("First Generation:")
print_stage(stage)
one_generation(stage)
print("Second Generation:")
print_stage(stage)