#To add a layer to the map, draw another layer using the same format,
#and reference in yaxislist. These are the only 2 references necessary.
yaxis0 = [' . ',' . ',' . ',' . ',' . ',' . ']
yaxis1 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis2 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis3 = [' . ',' X ',' . ',' . ',' o ',' . ',' . ',' . ']
yaxis4 = [' . ',' . ',' . ',' . ',' . ',' . ']


yaxislist = [yaxis0, yaxis1, yaxis2, yaxis3, yaxis4]
minyaxis = len(yaxislist)-1

userin = "setup placeholder"
global searchinterval, xaxis, yaxis
oldev = ' . '
ev = ' . '
searchinterval = 0
yaxis = 0
activeyaxis = yaxis0
tempyaxis = yaxis0

def axisfinder():
    global searchinterval, xaxis, yaxis
    xnotfound = True
    searchinterval = 0
    yaxis = 0
    xaxis = 0
    while xnotfound and searchinterval <= 1000:
        try:
            xaxis = yaxislist[searchinterval].index(' X ')
            yaxis = searchinterval
            xnotfound = False
        except:
            searchinterval = searchinterval + 1

def worlddisplay(minyaxisnum):
    interval = 0
    print("[][][][][][][][]")
    while interval <= minyaxisnum:
        print(*yaxislist[interval], sep='')
        interval = interval + 1
    print("[][][][][][][][]")

def eventfinder(eventcode):
    if eventcode == ' . ':
        #this would be a nested function if I was allowed to use them
        if "w" in userin or "s" in userin:
            tempyaxis.insert(xaxis, ' X ')
            del activeyaxis[xaxis]
        activeyaxis.insert(xaxis, oldev)
        worlddisplay(minyaxis)
    if eventcode == ' o ':
        if "w" in userin or "s" in userin:
            tempyaxis.insert(xaxis, ' X ')
            del activeyaxis[xaxis]
        activeyaxis.insert(xaxis, oldev)
        worlddisplay(minyaxis)
        print("you walked over the amazing test rock! congratulations!")

worlddisplay(minyaxis)

while userin != "quit":
    userin = input().lower()
    axisfinder()
    activeyaxis = yaxislist[yaxis]
    if userin == "test":
        print("test vacant")
    if userin == "axistest":
        axisfinder()
        print("yaxis: " + str(yaxis))
        print("xaxis: " + str(xaxis))
    if userin == "a":
        if xaxis != 0:
            oldev = ev
            ev = activeyaxis.pop(xaxis - 1)
            eventfinder(ev)
    elif userin == "d":
        if xaxis != len(activeyaxis)-1:
            oldev = ev
            ev = activeyaxis.pop(xaxis + 1)
            eventfinder(ev)
    elif userin == "w":
        if activeyaxis != yaxis0:
            try:
                tempyaxis = yaxislist[yaxis - 1]
                oldev = ev
                ev = tempyaxis.pop(xaxis)
                eventfinder(ev)
            except:
                print("There is nothing in that direction")
    elif userin == "s":
        if activeyaxis != yaxislist[minyaxis]:
            try:
                tempyaxis = yaxislist[yaxis + 1]
                oldev = ev
                ev = tempyaxis.pop(xaxis)
                eventfinder(ev)
            except:
                print("There is nothing in that direction")
