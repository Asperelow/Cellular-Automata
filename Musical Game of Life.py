import numpy as np
from matplotlib import pyplot as plt
from numba import jit
import simpleaudio as sa

# --------------------------- Adjustable Parameters ---------------------------------------#
iterations = 200                            # Total number if iterations to play
line_length = 10                            # How long all the rows should be
lines_per_note = 1                          # How many lines a single note takes
initial_percent_full = 30                   # What % of the board is initially populated
octaves_to_include = [1, 2, 3, 4, 5]        # The octaves to include in the audio
sec = 2                                     # The amount of time a single iteration is played
# ----------------------------------------------------------------------------------------#

musical_freqs = []                      # These few lines make it easier to include or exclude octaves
if len(octaves_to_include) != 0:
    if octaves_to_include[0] == 1:
        musical_freqs.append(32.7)
        musical_freqs.append(36.7)
        musical_freqs.append(41.2)
        musical_freqs.append(43.7)
        musical_freqs.append(49)
        musical_freqs.append(55)
        musical_freqs.append(61.7)
        octaves_to_include.pop(0)
if len(octaves_to_include) != 0:
    if octaves_to_include[0] == 2:
        musical_freqs.append(65.4)
        musical_freqs.append(73.4)
        musical_freqs.append(82.4)
        musical_freqs.append(87.3)
        musical_freqs.append(98)
        musical_freqs.append(110)
        musical_freqs.append(123.5)
        octaves_to_include.pop(0)
if len(octaves_to_include) != 0:
    if octaves_to_include[0] == 3:
        musical_freqs.append(130.8)
        musical_freqs.append(146.8)
        musical_freqs.append(164.8)
        musical_freqs.append(174.6)
        musical_freqs.append(196)
        musical_freqs.append(220)
        musical_freqs.append(246.9)
        octaves_to_include.pop(0)
if len(octaves_to_include) != 0:
    if octaves_to_include[0] == 4:
        musical_freqs.append(261.6)
        musical_freqs.append(293.7)
        musical_freqs.append(329.6)
        musical_freqs.append(349.2)
        musical_freqs.append(392)
        musical_freqs.append(440)
        musical_freqs.append(493.8)
        octaves_to_include.pop(0)
if len(octaves_to_include) != 0:
    if octaves_to_include[0] == 5:
        musical_freqs.append(523.3)
        musical_freqs.append(587.3)
        musical_freqs.append(659.3)
        musical_freqs.append(698.4)
        musical_freqs.append(784)
        musical_freqs.append(880)
        musical_freqs.append(987.8)
        octaves_to_include.pop(0)
musical_freqs = np.array(musical_freqs)


populated_test_vals = np.array([2, 3])      # Criteria for a living cell to continue living
unpopulated_test_vals = np.array([3])       # Criteria for a dead cell to start living
kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]])               # A neat kernel used for the convolution
height, width = lines_per_note * len(musical_freqs), line_length    # Creates height and width parameters
test_vals = np.concatenate((populated_test_vals + 10, unpopulated_test_vals), axis=0)

fs = 44100  # Sampling Frequency
t = np.linspace(0, sec, int(sec * fs))
window_han = np.hanning(len(t))             # Creates a hanning window to reduce clipping


# Almost a normal convolution function, but as it is iterating through it checks to see if the
# current cell should or shouldn't be populated on the next iteration.
### @jit()
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


# Creates sinewaves with a specific magnitude and frequency
def note_generator(freq, mag):
    return mag * np.sin(freq * t * 2 * np.pi)


game_board = np.random.randint(100, size=(height, width))       # Creates the initial game board
game_board = (game_board < initial_percent_full).astype(int)    # based on tunable parameters
game_boards = []
for i in range(iterations):
    game_boards.append(game_board)          # Keeps track of all the past states
    game_board = conv_2D_Conway(game_board) # Updates the game board


# This loop combines lines when necessary to assign each pitch a magnitude
mags = []
for board in game_boards:
    magnitudes_processed = []
    magnitudes_unprocessed = np.sum(board, axis=1)
    for i in range(int(len(magnitudes_unprocessed + 1) / lines_per_note)):
        magnitudes_processed.append(np.sum(magnitudes_unprocessed[i * lines_per_note:
                                                                  (i * lines_per_note) + lines_per_note]))
    mags.append(magnitudes_processed)

# This loop creates an output of all the states stitched together with hanning windows
for mags_done, mag_vec in enumerate(mags):
    freq_sum = note_generator(musical_freqs[0], mag_vec[0])
    for i in range(len(mag_vec) - 1):
        freq_sum += note_generator(musical_freqs[i + 1], mag_vec[i + 1])
    if mags_done == 0:
        output = freq_sum * window_han
    else:
        output = np.concatenate((output, np.zeros(int(len(window_han) * 0.5))), axis=0)
        output[(len(output) - len(window_han)):] += (freq_sum * window_han)


audio = output * (2 ** 15 - 1) / (np.max(np.abs(output)))   # Normalizes the output to 16-bits
audio = audio.astype(np.int16)                              # Converts the audio to 16-bit integers
play_obj = sa.play_buffer(audio, 1, 2, fs)                  # Plays the processed output
play_obj.wait_done()
