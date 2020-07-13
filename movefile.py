import shutil
import os
#import glob
import glob

source = 'C:/Users/acer/hps/'
dst = 'C:/Users/acer/txt/'
files = glob.iglob(os.path.join(source, "*.csv"))
#print(files)
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst)
        print("file berhasil dipindahkan")
    else :
        print("File kosong")