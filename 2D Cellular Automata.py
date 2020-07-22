import numpy as np
from matplotlib import pyplot as plt
from numba import jit


# ----------------------------- Adjustable Parameters---------------------------------------#
iterations = 500            # Number of iterations to go through
height = 200                # Height of the game board
width = 200                 # Width of the game board
initial_percent_full = 30   # What percent of the initial game board is populated
pop_criteria = np.array([3, 4]) # Similar to the rule in a 1D cellular automata, these
unpop_criteria = np.array([3])  # parameters dictate how the game progresses
# ------------------------------------------------------------------------------------------#


kernel = np.ones((3, 3))    # this kernel is used to find populated and unpopulated cells, then
kernel[1, 1] = 10           # figure out if surrounding cells are populated or not
pop_criteria += 10
test_vals = np.concatenate((pop_criteria, unpop_criteria), axis=0)


##@jit()
def conv_2D_Conway(img):
    conv_img = np.zeros_like(img)
    img = np.pad(img, pad_width=1, constant_values=0)
    for x in range(img.shape[1] - 2):
        for y in range(img.shape[0] - 2):
            img_slice = img[y:y + 3, x:x + 3]
            img_slice_conv = np.sum(img_slice * kernel)

            state = 0
            for test_val in test_vals:
                if test_val == img_slice_conv:
                    state = 1
            conv_img[y, x] = state

    return conv_img


game_board = np.random.randint(100, size=(height, width))   # Initializes the game board
game_board = (game_board < initial_percent_full).astype(int)

for i in range(iterations):
    game_board = conv_2D_Conway(game_board)
    plt.imshow(game_board, cmap=plt.cm.binary)
    plt.show(block=False)
    plt.pause(0.4)
