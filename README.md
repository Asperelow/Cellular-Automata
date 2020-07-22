# Cellular-Automata
## What is a Cellular Automata?
In short, a cellular automata is a zero-player game that progresses indefiantly. A 1-D cellular automata slowly grows with each iteration, and all of the previous generations are typically displayed at once (usually creating a triangle-like figure). A 2-D cellular automata usually remains the same size, and each iteration is displayed over the previous one. The most famous example of a 2-D cellular automta is Conways Game of Life, which is certain set of rules that allows for a balanced ending. Every pixel in a cellular automata updates with respect the the pixels, given a set of rules. For example, in Conways Game of Life, a populated cell will remain populated iff there are two or three populated cells surrounding it. An unpopulated cell will become populated iff there are three populated cells surrounding it. 

NOTE: I commented out the @jit() decorators, but if the numba library is installed then this can be undone.

# 1-D Cellular Automatas
## CellularAutomata.py
A basic, 1-D cellular Automata.
### Adjustable Parameters
**rule_num** - Which rule to follow                     (Default is 30, because it is the coolest)

**iterations** - The number of iterations to display    (Default is 100)

## Multicolor Cellular Automata
A slightly more complicated cellular automata. This one can have anywhere from two (the basic) to 38 colors. The total number of combinations is equal to (number of colors)^8.
### Adjsutable Parameters
**colors** - The numbers of colors to display           (Default is two, the simplest)

**rule_num** - Which rule to follow                     (Default is 30, because it is the coolest)

**iterations** - The number of iterations to display    (Default is 100)

# 2-D Cellular Automatas
 ## 2D Cellular Automata.py
 A simple 2-D cellular automata that progresses with time based on the populated and unpopulated criteria. The values that these parameters are set to will dictate which cells continue/become populated in the next generation.
 ### Adjustable Parameters
 **iterations** - the number of iterations to go through                (Default is 500)
 
 **height** - the height of the game board                              (Default is 200)
 
 **width** - the width of the game board                                (Default is 200)
 
 **initial_percent_full** - the percent of initally populated cells     (Default is 30)
 
 **pop_criteria** - criteria for populated cells to progress            (Default is 3 & 4, Conways Game of Life)
 
 **unpop_criteria** - criteria for unpopulated cells to progress        (Default is 3, Conways Game of Life)
 
 ## Musical Game of Life
 A 2-D cellular automata the is set to the parameters of Conways Game of Life, but the ouput is a mix of sinwaves from the first 5 octaves instead of a plot showing the populated and unpopulated values. Each generation is converted to audio, passed through a hanning window, then added to a running sum of each generation. The hanning windows are overlapped to eliminate clipping sounds due to the Gibbs effect. 
### Adjustable Parameters
 **iterations** - the number of iterations to go through                (Default is 500)
 
**line_length** - the width of the "game board"                         (Default is 10)

**lines_per_note** - the number of lines each note consists of          (Default is 1)

**initial_percent_full** - the percent of inially populated cells       (Default is 30)

**octaves_to_incluce** - which octaves to include in the output, 1-5    (Default is all)

**sec** - how many seconds each generation lasts                        (Default is 2, but first and last 0.5 seconds are transitions)  


















