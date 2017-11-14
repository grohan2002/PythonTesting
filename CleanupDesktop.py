import shutil
import os

input = raw_input('Enter the directory to scan >> ')
source = '/Users/rohangupta/' + input
#typeOfFile = raw_input('Enter the type of file to move ')
input2 = raw_input('Enter the type of files to move >> ')
path = '/Users/rohangupta/Documents/' + input2.upper()

if not os.path.exists(path):
    os.makedirs(path)

FileMap = {'csv': '/Users/rohangupta/Documents/CSV',
             'txt': '/Users/rohangupta/Documents/TXT',
              }

if input2 not in FileMap:
    FileMap[input2] = '/Users/rohangupta/Documents/' + input2


files = os.listdir(source)


for f in files:
    for key, value in FileMap.iteritems():
        #if key in f.lower():
        if (f.endswith(key)):
            path = source + '/' + f
            #shutil.move(f, path + '/' + value)
            shutil.move(path, value)
        else:
            print 'Error identifying vendor for', f



