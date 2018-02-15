import os
# All this does is open the data file in the variable called 'filetext'
# Still need to write the parser for the files

fileDir = os.path.dirname(os.path.realpath('__file__'))
dataname='Data/reut2-000.sgm'
filename = os.path.join(fileDir, dataname)
print "opening " + filename
f = open(filename, 'r')
filetext = f.read()


