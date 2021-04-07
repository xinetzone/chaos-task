from wand.image import Image as WImage
from zipfile import ZipFile
from nbconvert import PDFExporter, HTMLExporter
import shutil

def zip_sol():
    shutil.make_archive('A2-sol', 'zip', base_dir='supplements')
    with ZipFile('A2-sol.zip', 'a') as zipfile:
        zipfile.write('cover.ipynb', 'cover.ipynb')
        zipfile.write('Q1.ipynb', 'Q1.ipynb')
        zipfile.write('Q2.ipynb', 'Q2.ipynb')
        zipfile.write('Q3.ipynb', 'Q3.ipynb')
        zipfile.write('Q4.ipynb', 'Q4.ipynb')

    print('## created A2-sol.zip containing the following files ##')
    with ZipFile('A2-sol.zip', 'r') as zipObj:
       listOfiles = zipObj.namelist()
       for elem in listOfiles:
           print(elem)

def show_file(filename, pages=[0], scale=1):
    '''
    Display selected pages from a file at a chosen scale.
    '''
    for i in pages:
        img = WImage(filename="%s[%d]" % (filename, i), resolution=100)
        img.resize(width=int(scale*img.width), height=int(scale*img.height))
        display(img)
