#To add a layer to the map, draw another layer using the same format,
#and reference in yaxislist. These are the only 2 references necessary.
yaxis0 = [' . ',' . ',' . ',' . ',' . ',' . ']
yaxis1 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis2 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis3 = [' . ',' X ',' . ',' . ',' o ',' . ',' . ',' . ']
yaxis4 = [' . ',' . ',' . ',' . ',' . ',' . ']

#creates a multidimensional array
yaxislist = [yaxis0, yaxis1, yaxis2, yaxis3, yaxis4]
minyaxis = len(yaxislist)-1 #finds the value of the lowest y-axis

#variable incantations
userin = "setup placeholder"
global searchinterval, xaxis, yaxis
oldev = ' . '
ev = ' . '
searchinterval = 0
yaxis = 0
activeyaxis = yaxis0
tempyaxis = yaxis0

#sets up axisfinder, a function which locates the X on the grid
def axisfinder():
    global searchinterval, xaxis, yaxis #recieves globals
    xnotfound = True # sets boolean to false
    searchinterval = 0 # resets searchinterval
    yaxis = 0 #resets yaxis
    xaxis = 0 #resets xaxis
    while xnotfound and searchinterval <= 1000: # sets while criteria
        try: #if it can run the following:
            #sets x to be equal to the index of the currently searched list
            xaxis = yaxislist[searchinterval].index(' X ')
            yaxis = searchinterval # yaxis is equal to currently searched yaxis
            xnotfound = False # boolean set to false to cancel while
        except: #if the previous could not be run:
            searchinterval = searchinterval + 1 #add 1 to search interval

#prints the world map with a revieved value of the minimum yaxis to be printed
def worlddisplay(minyaxisnum):
    interval = 0 #incantates interval
    print("[][][][][][][][]") #prints a sweet border
    #while the interval is smaller than the accepted value:
    while interval <= minyaxisnum:
        print(*yaxislist[interval], sep='') #print the yaxis w/o any list stuff
        interval = interval + 1 #add 1 to interval
    print("[][][][][][][][]") #prints a vibing border

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
