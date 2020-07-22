import numpy as np
from matplotlib import pyplot as plt
from numba import jit


# ----------------------------- Adjustable Parameters---------------------------------------#
rule_num = 30
iterations = 100
# ------------------------------------------------------------------------------------------#


def next_gen_calculator():
    next_gen = np.zeros((1, len(current_gen)))
    for pos in range(len(current_gen) - 2):
        real_pos = pos + 1
        rule_eval = current_gen[real_pos - 1:real_pos + 2]
        rule_eval = str(int(rule_eval[0])) + str(int(rule_eval[1])) + str(int(rule_eval[2]))
        rule_number = 7 - int(rule_eval, base=2)
        next_gen[0, real_pos] = rule[rule_number]
        print(rule_eval)
    return next_gen


def zero_edge(input_state):
    zero_vector = np.zeros((input_state.shape[0], 1))
    return np.concatenate((zero_vector, input_state, zero_vector), axis=1)


state = np.array([[0, 1, 0]])                   # Initializes the state of the game board
rule = bin(rule_num)[2:]                        # Converts the rule number to a list of the outputs
rule = list('0' * (8 - len(rule)) + rule)

for i in range(iterations):
    state = zero_edge(state)                    # Pads the edges of the game board with zeros for the next generation
    current_gen = state[i]                      # Declares the current generation
    next_gen_result = next_gen_calculator()     # Finds the results of the next generation
    state = np.concatenate((state, next_gen_result), axis=0)
plt.imshow(state, cmap=plt.cm.binary)           # Displays the results
plt.show()
