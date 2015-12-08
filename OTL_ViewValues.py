# This script is for CE 531 to analyze the stochastic analysis graphs created by
# the GSSHA model in WMS. It will read the different *.otl files (they are shorter
# than the *.ohl files) and create a final *.csv file that can be used to
# simultaneously compare the different output hydrographs.

# You are free to use/modify this script, however, you do so at your own risk.
# Intended only for WMS GSSHA Stochastic analysis only.
# Created/Uploaded 8Dec2015

import os
import csv

Folder = "C:\\Users\\Stephen\\Documents\\01-CurrentClassFolders\\CE 531 Hydrologic Modeling\\Project\\BaseStephen\\GSSHABase_StochasticRUN3_StochOutput"
OTL = ".otl"
OTLlist = []
count = 0
#listedOTLlist= []
myViewingList = []

# First, figure out the list of files in the Folderlist
GSSHAlist = os.listdir(Folder) #This is the file list
# Second, loop through the files to extract data
for StochFile in GSSHAlist:
    # Test for .otl in filename
    myOTLtest = StochFile.find(OTL)
    # If myOTLtest >= 0, then it is an *.otl filetype
    if myOTLtest >= 0:
        OTLlist.append(StochFile)
# test for finding files, if needed
#print OTLlist
for OTLfile in OTLlist:
    # Open the *.otl file
    openOTL = open(Folder + "\\" + OTLfile)
    # Read the *.otl file as a list with each line being listed
    openOTLlist = []
    openOTLlist = openOTL.readlines()
    #print openOTLlist
    # get Rid of the /n in the strings from the list
    openOTLlist = [line.rstrip('\n') for line in openOTLlist]
    #print openOTLlist
    # Split based on the white space.
    listedOTLlist= []
    for myRow in openOTLlist:
        listedOTLlist.append(myRow.split())
    #print listedOTLlist
    # Now when count = 0, make the first item in each list the time
    if count == 0:
        for myLittleList in listedOTLlist:
            myViewingList.append([myLittleList[count]])
        #print myViewingList
        count = 1 #should stay true for rest of time
    # Then after time list is created, we need to add the values to each list.

    if count == 1:
        placeholder = 0
        for myTime in myViewingList:
            #print myTime
            try: #if myDataLine exists
                myDataLine = listedOTLlist[placeholder]
            except: #if myDataLine doesn't exist
                myDataLine = ['0','0']
            #print myDataLine
            myTime.append(myDataLine[count])
            placeholder = placeholder + 1
    # All done with current *.otl file. Close and move to next.
    openOTL.close()
#print listedOTLlist
# test final list for values and continuity
print myViewingList
# Create a heading row for CSV
myHeader = ['Time']
myHeader.extend(OTLlist)
#print myHeader
# Now create the csv file for viewing!
myCSVfile = Folder + "\\00000_ViewValues.csv"
openCSVfile = open(myCSVfile,'wb')
writeCSVfile = csv.writer(openCSVfile)
# Write header line first
writeCSVfile.writerow(myHeader)
for myFinalList in myViewingList:
    writeCSVfile.writerow(myFinalList)
openCSVfile.close()
print "Done!"
