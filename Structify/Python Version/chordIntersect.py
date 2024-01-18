__author__="Jason Durek"
__dateChanged__="1/17/2024"

import math

# Main function for handling Chord Intersections - 
def chordIntersections(chords)->int:
    if not chords:
        return 0
    
    chordCount:int = 0
    for x, chord in enumerate(chords):
        # Check if they intercept previous chords (Use x for index)
        print(chord, x)
        for i in range(x):
            # Check if they intercept, increment chordCount if they do
            if intercepts(chord[0], chord[1], chords[i][0], chords[i][1]):
                chordCount += 1
            continue
    return chordCount

# Parses input format into array of tuples (start,end)
# This also converts from radian format to cartesian coordinates so we can just do intersections using those
def parseInput(input):
    # If there's a mismatching number of inputs, terminate early
    coordList = input[0]
    pairList = input[1]
    if len(coordList) %2 != 0:
        print("Odd number of coordinates provided - one line is missing endpoint")
        return

    endpoints:[(float,float)] = []
    chords:[((float, float), (float,float))] = []

    # Current expected input format is a tuple made of 2 arrays, sorted by the 1st array - 
    # Sort it on the 2nd array, then convert into line segment start/end tuple
    # Silly method for sorting it - 's' becomes just the number, and 'e' is equal to adding 0.5 to it, then we sort
    transformedPairs = list(map(endptCvt, pairList))
    # Sort coordinates based on our transformed pairs
    transformedPairs, coordList = zip(*sorted(zip(transformedPairs, coordList)))
    
    # Convert from polar coordinates (Radians) to Cartesian coordinates
    # the 4 is just an arbitrary radius for the circle to make visualization easier if needed
    for coord in coordList:
        endpoints.append(( 4*math.cos(coord), 4*math.sin(coord) ))
    for i in range(int(len(endpoints)/2)):
        chords.append((endpoints[i],endpoints[i+1]))
    print(chords)
    return chords

# Simple function to transform endpoint data from s/e notation to pure numbers
def endptCvt(endpoint):
    if endpoint[0] == 's':
        return int(endpoint[1:])
    elif endpoint[0] == 'e':
        return int(endpoint[1:]) + .5
    

# These two functions handle the intersections - they don't handle colinearity, but with our restrictions - don't need to worry about it
def orientation(a, b, c):
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] * a[0])

def intercepts(a,b,c,d):
    return (orientation(a, c, d) != orientation(b, c, d) and orientation(a,b,c) != orientation(a,b,d))

if __name__ == "__main__":
    # Test Example #1
    inTest1 = [(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")]
    chords = parseInput(inTest1)
    intersects = chordIntersections(chords)
    print ("%s intercepts with input args" % intersects)
    # Test Example #2
    inTest2 = [(0.00, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6), ("e1", "s1", "s2", "e3", "s3", "e2")]
    chords = parseInput(inTest2)
    intersects = chordIntersections(chords)
    print ("%s intercepts with input args" % intersects)
    pass