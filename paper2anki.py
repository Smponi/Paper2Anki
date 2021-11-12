import glob
import os
import re
import shutil
import sys
import time

import fitz
from PIL import Image
from pdfrw import PdfReader, PdfWriter, PageMerge

from AnkiCreator import create_apkg

TEMP = "Temp"
if not os.path.exists(TEMP):
    os.makedirs(TEMP)

"""
Split a page into two (top and bottom)
Source: https://stackoverflow.com/a/31640152/5861086
credits to Patrick Maupin
I have modified it, so the pages do not contain empty block
"""


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
    writer.write(TEMP + os.sep + "input.pdf")


def create_images():
    current_time_in_millis = str(int(time.time_ns()))
    zoom_x = 2.0  # horizontal zoom
    zomm_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zomm_y)  # zoom factor 2 in each dimension
    doc = fitz.open(TEMP + os.sep + "input.pdf")
    for x in doc:
        pix = x.get_pixmap(alpha=False, matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # To make every image name in each file unique we will use the unix timestamp of the current day as a name extra
        img.save(
            "%s%s.jpg"
            % (TEMP + os.sep, format(x.number, "04d") + "-" + current_time_in_millis)
        )


def rename_files():
    regex = r"[0-9]+\.jpg"
    filelist = glob.glob("Temp" + os.sep + "*.jpg")
    for filename in filelist:
        x = re.search(regex, filename)
        os.rename(str(filename), "Temp" + os.sep + x.group())


def remove_temp():
    try:
        shutil.rmtree(TEMP)
    except OSError as e:
        print(f"Error: {TEMP} : {e.strerror}")


if __name__ == "__main__":
    pdf = sys.argv[1]
    name = sys.argv[2]
    createPDF(pdf)
    create_images()
    create_apkg(name)
    remove_temp()
