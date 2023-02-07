import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
fileNames = glob.glob(pattern+'.*')
# print(fileNames)

# TODO: use os.path.getsize to find each file's size
for eachFile in fileNames:
    fileSize = os.path.getsize(eachFile)
    print(eachFile, fileSize)

# TODO: Add a test to only display files that are not zero length
for eachFile in fileNames:
    if os.path.getsize(eachFile) > 0:
        print(eachFile)

# TODO: Remove the leading directory name(s) from each filename before you print it -
for eachFile in fileNames:
    if os.path.getsize(eachFile) > 0:
        print(os.path.basename(eachFile))
#        print(os.path.basename(eachFile), os.path.getsize(eachFile))
