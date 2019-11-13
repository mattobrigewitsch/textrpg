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
        if "w" in userin or "s" in userin: #only runs next lines if met
            tempyaxis.insert(xaxis, ' X ') #if going up or down insert a new X
            del activeyaxis[xaxis] #delete old X
        activeyaxis.insert(xaxis, oldev) #insert the missing map part
        worlddisplay(minyaxis) #draw the map
    if eventcode == ' o ':
        if "w" in userin or "s" in userin:#only runs next lines if met
            tempyaxis.insert(xaxis, ' X ')#if going up or down insert a new X
            del activeyaxis[xaxis]#delete old X
        activeyaxis.insert(xaxis, oldev)#insert the missing map part
        worlddisplay(minyaxis)#draw the map
        print("you walked over the amazing test rock! congratulations!")

worlddisplay(minyaxis) #initial display function, for initialization

while userin != "quit": #consistently run the following
    userin = input().lower() #take user input in lower case
    axisfinder() #find the X
    activeyaxis = yaxislist[yaxis] #set the activeyaxis to the y axis with the X
    if userin == "test": #test code, n/a
        print("test vacant")
    if userin == "axistest": #used for testing again, n/a
        axisfinder()
        print("yaxis: " + str(yaxis))
        print("xaxis: " + str(xaxis))
    if userin == "a": #if user types a
        if xaxis != 0: #if the X isnt on the edge
            oldev = ev #change old event
            ev = activeyaxis.pop(xaxis - 1) #change new event
            eventfinder(ev) #run eventfinder with new event
    elif userin == "d": #if user types d
        if xaxis != len(activeyaxis)-1: #if the X isnt on the edge
            oldev = ev #change old event
            ev = activeyaxis.pop(xaxis + 1) #change new event
            eventfinder(ev) #run eventfinder with new event
    elif userin == "w": #if user types w
        if activeyaxis != yaxis0: #if the X isnt on the edge
            try: #try to run the following
                tempyaxis = yaxislist[yaxis - 1] #create a temporary new y axis
                oldev = ev #change old event
                ev = tempyaxis.pop(xaxis) #change new event
                eventfinder(ev) #run eventfinder with new event
            except: #run if the try failed:
                #the only reason the try should fail is because there is nothing
                #in the direction
                print("There is nothing in that direction")
    elif userin == "s": #if user types s
        if activeyaxis != yaxislist[minyaxis]: #if the X isnt on the edge
            try: #try to run the following
                tempyaxis = yaxislist[yaxis + 1] #create a temporary new y axis
                oldev = ev #change old event
                ev = tempyaxis.pop(xaxis) #change new event
                eventfinder(ev) #run eventfinder with new event
            except:#run if the try failed:
                #the only reason the try should fail is because there is nothing
                #in the direction
                print("There is nothing in that direction")
    else: #run if the input is not in range of anything prior
        worlddisplay(minyaxis) #draw map
        print("invalid input") #print invalid input to console
