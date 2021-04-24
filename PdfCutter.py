from AnkiCreator import createAPKG
import sys
import os,glob
import re
from pdfrw import PdfReader, PdfWriter, PageMerge
from pdf2image import convert_from_path



TEMP = "Temp"
if not os.path.exists(TEMP):
    os.makedirs(TEMP)

''' 
Split a page into two (top and bottom)
Source: https://stackoverflow.com/a/31640152/5861086
credits to Patrick Maupin
I have modified it, so the pages do not contain empty block
'''
def splitpage(src):
    for y_pos in (0, 0.5):
        # Create a blank, unsized destination page.
        page = PageMerge()
        page.add(src, viewrect=(0, y_pos, 1, 0.5))
        yield page.render()        
def createPDF(pdf):
    writer = PdfWriter()
    for page in PdfReader(pdf).pages:
        writer.addpages(splitpage(page))
    writer.write(TEMP+"/input.pdf")

def createImages():
    convert_from_path(TEMP+"/input.pdf", output_folder=TEMP,fmt="jpeg",thread_count=os.cpu_count())
def renameFiles():
    regex = r"[0-9]+\.jpg"
    filelist = glob.glob('Temp/*.jpg')
    for filename in filelist:
        x = re.search(regex,filename)
        os.rename(str(filename),"Temp/"+x.group())    


if __name__ == '__main__':
    pdf = sys.argv[1]
    name = sys.argv[2]
    createPDF(pdf)
    createImages()
    renameFiles()
    createAPKG(name)
