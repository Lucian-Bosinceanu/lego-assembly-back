
# Implementation idea :
# 1. Pick a random brick, generate a valid set of neighbors
# 2. Try to merge the brick with the neighbor that will result in the largest possible piece available
# 3. Go to Step 2 untill neighbours set is empty or no further merges can be done
# 4. Go to Step 1 untill no change can be done.
#
# Mentions:
# 1. Define a legal set of bricks outside this folder (as they are needed in multiple places)
# and use it when chosing the neighbor to merge with
# 2. To efficiently randomize the brick choice :
#       - Create a set with all bricks, do all the following on a copy of it
#       - Pick a random brick, apply Step 2 and remove the brick from the set. Mark if any merge was made
#       - When the set is empty, clone the set again and apply the random algorithm again
#       - Stop when the set is empty and no merge has been made


def merge_cubes(shape):
    pass