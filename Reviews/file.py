# Example module script in py2.7
# Tui Britton
# Created: March 2017
# Last Modification: March 2017
######################################################################
# Import standard modules
import os
import sys

#Play with some command line code
def listFile(file_type):
     print "Listing files..."
     os.system('ls *.%s' % (file_type))
     print "Files loaded!"

######################################################################

