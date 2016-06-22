# this module provides access to command line arguments
import sys

filename = sys.argv[1]


# given a symbol at position i in LastColumn, what is its position in FirstColumn?
def LastToFirst(FirstColumn, LastColumn):

    ret = list()
    LastColumnCopy = list()
    start_at = { }

    #  Hash start_at keeps a mapping of which index to start the search for
    #  the next occurrence of char c in firstColumn
    for c in LastColumn:
        LastColumnCopy.append(c)
        start_at[c] = 0

    # for each character in LastColumn, find the first occurrence of it in FirstColumn
    # starting search at previously found index of c

    for c in LastColumn:
        for i in range(start_at[c], len(LastColumn)):
            if(FirstColumn[i] == c):

                start_at[c] = i + 1
                ret.append(i)
                break


    return ret

def BWMatching(FirstColumn, LastColumn, Pattern, Mapping):

    top = 0
    bottom = len(LastColumn) - 1

    while top <= bottom:
        if(Pattern != ""):
            symbol = Pattern[len(Pattern)-1:len(Pattern)]
            Pattern = Pattern[0:len(Pattern) - 1]

            topIndex = -1
            botIndex = -1

            for i in range(top, bottom + 1):
                if(LastColumn[i] == symbol):
                    if(topIndex == -1):
                        topIndex = i
                        botIndex = i
                    else:
                        botIndex = i

            if(topIndex != -1):
                top = mapping[topIndex]
                bottom = mapping[botIndex]
            else:
                return 0
        else:
            return bottom - top + 1


with open(filename, 'r') as f:


    BWT = f.readline().strip('\n')
    Patterns = f.readline().split(" ")

    arr = list()

    FirstColumn = list()
    LastColumn = list()

    for i in range(0, len(BWT)):
        FirstColumn.append(BWT[i])
        LastColumn.append(BWT[i])

    FirstColumn.sort()

    # create LastToFirst mapping
    mapping = LastToFirst(FirstColumn, LastColumn)


    for p in Patterns:
        arr.append(BWMatching(FirstColumn, LastColumn, p, mapping))

    ret = ""
    for i in arr:
        ret += str(i) + " "
    ret = ret[:-1]

    f2 = open("output.txt", 'w')
    f2.write(ret)












