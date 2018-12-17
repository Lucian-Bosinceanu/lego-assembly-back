# Implementation idea :
1. Pick a random brick, generate a valid set of neighbors
2. Try to merge the brick with the neighbor that will result in the largest possible piece available
3. Go to Step 2 until neighbours set is empty or no further merges can be done
4. Go to Step 1 until no change can be done.

# Mentions:
1. Define a legal set of bricks outside this folder (as they are needed in multiple places)
and use it when choosing the neighbor to merge with
2. To efficiently randomize the brick choice :
    - Create a set with all bricks, do all the following on a copy of it
    - Pick a random brick, apply Step 2 and remove the brick from the set. Mark if any merge was made
    - When the set is empty, clone the set again and apply the random algorithm again
    - Stop when the set is empty and no merge has been made
    
# Genetic Algorithm Representation of the Lego Brick merging problem
For simplicity we reduced the merging problem for each level, therefore the algorithm will apply for each level in the current shape model.

## Chromosomes 
The candidate solution is represented by a matrix of merged cubes. The algorithm for merging cubes is as follows:
1. Pick a random brick, look through his neighbors and pick a random one
2. Try to merge the brick with the neighbor 
3. Go to Step 2 until no more merges can be done in the current matrix

The fitness function should reflect how close to the target chromosome (best solution) we are. In this case we chose a 
fitness function f(x) = count(cubes that were not merged). In our problem the best solution is represented by the fewer unmerged bricks
(the more we merge the better the solution for the current level will be)

## Population
The population consists of a set of chromosomes after n generations evolved (0 < n < GENERATION_COUNT)
After each iteration we will be choosing 2 best fit chromosome to merge and remove the worst fit chromosome from the set 
(we will apply natural selection concept or a process that is better known as crossover population)
*Crossover* algorithm will be done follows:
1. Pick the 2 best fit chromosome then: 
  * Pick a random brick from the first chromosome and add him and all merged neighbours with it to the new chromosome
  * Add all the left pieces from the second chromosome to the newly created chromosome
2. Remove the worst fit chromosomes so we have the same population size

The crossover process will be followed by a selection of individuals for next iteration and be repeated for GENERATION_COUNT times

# Implementation details
## `LevelMatrix` 
Contains info about current level matrix and handles merging of the bricks on the current level matrix
## `Chromosome` 
Contains info about one candidate solution, building algorithm described earlier should be found inside `build` method
