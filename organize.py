import os
import shutil

from_dir = 'C:\Users\Shaurya\Downloads'
to_dir = 'C:\Users\Shaurya\Downloads\White Hat jr\DownlodedImages'

listoffiles = os.listdir(from_dir)
#print(listoffiles)

for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir+'/'+filename
        path2 = to_dir+'/'+'imagefiles'
        path3 = to_dir+'/'+'imagefiles'+'/'+filename

    if os.path.exists(path2):
        print('moving'+filename+'...')
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print('moving'+filename+'...')
        shutil.move(path1,path3)

