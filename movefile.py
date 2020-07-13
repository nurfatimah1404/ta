import shutil
import os
#import glob
import glob

source = '/home/data/post/'
dst = '/home/data/mvfile/'
files = glob.iglob(os.path.join(source, "*.csv"))
#print(files)
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst)
        print("file berhasil dipindahkan")
    else :
        print("File kosong")