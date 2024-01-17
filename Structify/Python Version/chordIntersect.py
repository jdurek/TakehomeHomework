__author__="Jason Durek"
__dateChanged__="1/17/2024"


# Main function for handling Chord Intersections - 
def chordIntersections(chords):
    for chord in chords:
        # Check if they intersect all previous chords, OR check if they intercept all future chords
        continue
    return 0

# Parses input format into array of tuples (start,end)
# This also converts from radian format to cartesian coordinates so we can just do intersections using those
def parseInput(input):
    # If there's a mismatching number of inputs, terminate early
    if len(input[0]) %2 != 0:
        print("Odd number of coordinates provided - one line is missing endpoint")
        return
    
    # If the startpoint and endpoint chars differ, also terminate if necessary

    chords:[(float,float)] = []

    # Current expected input format is a tuple made of 2 arrays, sorted by the 1st array - 
    # Sort it on the 2nd array (string), then convert into line segment start/end tuple

    return chords


if __name__ == "__main__":
    # Test Example #1
    inTest1 = [(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")]

    # Test Example #2

    pass