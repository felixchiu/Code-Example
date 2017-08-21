import os
import hashlib
import time
import shutil

img_folder = '/Volumes/1T Movies/Data Recovery 2015-03-23 at 19.51.08/Image/jpg'
tgt_root = '/Users/fchiu/tmp/pictures'

row = 0
for path, subdirs, files in os.walk(img_folder):
    for name in files:
        filename = os.path.join(path, name)
        print "created : %s" % time.ctime(os.path.getctime(filename))
        image_file = open(filename).read()
        hx = hashlib.md5(image_file).hexdigest()
        prefix = time.strftime("%Y/%m/%d/%H/%M/%S", time.localtime(os.path.getctime(filename)))
        tgt_folder = tgt_root + "/" + prefix
        try:
            os.makedirs(tgt_folder)
        except OSError, e:
            print "Same second picture..."
        tgt_file = tgt_folder + "/" + hx + name
        shutil.copyfile(filename, tgt_file)
        print "Hash value: %s" % hx
        row = row + 1

print "Number of rows %d" % row
