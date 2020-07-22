import numpy as np
from matplotlib import pyplot as plt
from numba import jit


# ----------------------------- Adjustable Parameters---------------------------------------#
colors = 2
rule_num = 30
iterations = 100
# ------------------------------------------------------------------------------------------#


#@jit()
def dec_to_base(num, base):
    converted_string = ""
    while num:
        mod = num % base
        num = num // base
        converted_string = chr(48 + mod + 7 * (mod > 10)) + converted_string
    return converted_string


#@jit()
def next_gen_calculator():
    next_gen = np.zeros((1, len(current_gen)))
    for pos in range(len(current_gen) - 2):
        real_pos = pos + 1
        rule_eval = current_gen[real_pos - 1:real_pos + 2]
        rule_eval = str(int(rule_eval[0])) + str(int(rule_eval[1])) + str(int(rule_eval[2]))
        rule_number = (colors3 - 1) - int(rule_eval, base=colors)
        next_gen[0, real_pos] = rule[rule_number]
    return next_gen


#@jit()
def zero_edge(input_state):
    zero_vector = np.zeros((input_state.shape[0], 1))
    return np.concatenate((zero_vector, input_state, zero_vector), axis=1)


colors3 = colors ** 3                       # A reoccurring number
state = np.array([[0, 1, 0]])               # Initializes the rules and game board
rule = dec_to_base(rule_num, colors)        # Converts the input number into a list of outcomes for the rules
rule = list('0' * (colors3 - len(rule)) + rule)

for i in range(iterations):
    state = zero_edge(state)                # Pads the edges with zeros for the next iteration
    current_gen = state[i]                  # Declares the current generation
    next_gen_result = next_gen_calculator() # Updates the game board
    state = np.concatenate((state, next_gen_result), axis=0)
plt.imshow(state, cmap=plt.cm.rainbow)      # Displays the output
plt.show()
