
#To add a layer to the map, draw another layer using the same format,
#and reference in yaxislist. These are the only 2 references unecessary.
yaxis0 = [' . ',' . ',' . ',' . ',' . ']
yaxis1 = [' . ',' . ',' . ',' . ',' . ']
yaxis2 = [' . ',' . ',' . ',' X ',' . ']
yaxis3 = [' . ',' . ',' . ',' . ',' . ']
yaxis4 = [' . ',' . ',' . ',' . ',' . ']

yaxislist = [yaxis0, yaxis1, yaxis2, yaxis3, yaxis4]
minyaxis = len(yaxislist)-1
print(minyaxis)

activeyaxis = 0 #only test use, outdated var
userin = "setup placeholder"
global searchinterval, xaxis
searchinterval = 0

def axisfinder():
    global searchinterval, xaxis
    xnotfound = True
    while xnotfound:
        try:
            xaxis = yaxislist[searchinterval].index(' X ')
            activeyaxis = searchinterval
            xnotfound = False
        except:
            xnotfound = True #unecessary line of code
            searchinterval = searchinterval + 1

def worlddisplay(minyaxisnum): #    print(*yaxislist[0], sep='')
    interval = 0
    print("[][][][][][][][]")
    while interval <= minyaxisnum:
        print(*yaxislist[interval], sep='')
        interval = interval + 1
    print("[][][][][][][][]")

worlddisplay(minyaxis)

while userin != "quit":
    userin = input()
    if userin == "axistest":
        axisfinder()
        print("yaxis: " + str(searchinterval))
        print("xaxis: " + str(xaxis))
