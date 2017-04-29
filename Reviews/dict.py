# Example code taken from various scripts written by
# Tui Britton in Python 2.7 
# August 2011
# Modified March 2013
######################################################################
# Import standard modules
import os
import sys
import math

#Open a file, read in the data, create a dictionary
def chooseFreq(day):
          # User input
          config = int(raw_input("Please enter the configuration number you want to reduce: "))
          print "Chosen configuration number: ", config

          # Initialise frequency list by choosing text file (use tab delimied txt) for chosen configuration
          configfile = "%s_config%i.txt" % (day,config)
          print "The file you have chosen is: ", configfile
          with open(configfile,'rU') as freqList: #interprets mac line endings in unix

               # Create frequency dictionary based on the configuration chosen
               restfreqDict={}

               for line in freqList:
                    #ignore comments in txt file
                    if line.startswith("#"):
                         continue

                    #divide file into columns
                    columns = line.split()
                    if len(columns)!=3:
                         raise RuntimeError, "Expecting 3 columns in file, you have %i, please check your .txt file" % (len(columns))

                    #Define jline, line (observed) freq, and rest freq from columns
                    jline = int(columns[0]) 
                    linefreq = str(columns[1])
                    restfreq = float(columns[2])

                    #Put line and rest frequencies into dictionary using jline as key
                    restfreqDict[jline] = [linefreq,restfreq]
          
          #Check dictionary and cleanup
          print restfreqDict

          # User input to determine which raw data file from Miriad to use
          reduceline = int(raw_input("Please enter the Jline you want to reduce (2,3,4,5,6,7,8,9): "))
          print "Chosen jline: ", reduceline
          molecule = restfreqDict[reduceline]
          print molecule
          mollinefreq = str(molecule[0])
          molrestfreq = molecule[1]
          print "Chosen line frequency is: ", mollinefreq
          print "Chosen rest frequency is: ", molrestfreq
 
          return [mollinefreq,reduceline,config,molrestfreq]
     
######################################################################
