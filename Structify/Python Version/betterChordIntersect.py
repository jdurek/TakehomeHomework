# Amazing what you realize while falling asleep isn't it?

# Implementation of a better method for the chord intersection, which better matches the initial implementation's sorting
# Means we don't need to sort when accounting for our runtime notation

def chordIntersections(input)->int:
    numElems = len(input[0])
    chordCount = 0
    unfinishedChords = []
    print(numElems)
    for i in range(numElems):
        print(unfinishedChords)
        if input[1][i][0] == 's':
            # Append the ID of the chord (number/chars)
            unfinishedChords.append(input[1][i][1:])
        elif input[1][i][0] == 'e':
            # Iterate through unfinishedChords until we find the index that matches
            key = input[1][i][1:]
            for x, chord in enumerate(unfinishedChords):
                if chord == key:
                    # Add to chordCount based on how many chords were in between current index and end
                    chordCount += len(unfinishedChords) - 1 - x
                    # Remove the element at the index
                    del unfinishedChords[x]
                    break


    return chordCount


if __name__ == "__main__":
    # Test Example #1
    inTest1 = [(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")]
    intersects = chordIntersections(inTest1)
    print ("%s intercepts with input args" % intersects)
    # Test Example #2 - 2 points intersect on the edge of the circle (Same starting points)
    # Result - they're not "inside the circle", so they didn't intercept - returns 2 interceptions from vertical line
    inTest2 = [(0, 0, 1.5, 1.7, 2, 4), ("s1", "s2", "s3", "e3", "e2", "e1")]
    chords = chordIntersections(inTest2)
    print ("%s intercepts with input args" % intersects)