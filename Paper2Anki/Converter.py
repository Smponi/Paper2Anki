import glob
import os
import re
import shutil

import fitz
from PIL import Image
from loguru import logger
from pdfrw import PdfReader, PdfWriter, PageMerge


class Converter:
    TEMP = "Temp"

    def __init__(self, input_pdf: str, output_name: str) -> None:
        self.pdf = input_pdf
        self.name = output_name

    def __del__(self):
        self.remove_temp()

    def splitpage(self, src):
        """
        Split a page into two (top and bottom)
        Source: https://stackoverflow.com/a/31640152/5861086
        credits to Patrick Maupin
        I have modified it, so the pages do not contain empty block
        """

        for y_pos in (0, 0.5):
            # Create a blank, unsized destination page.
            page_merger = PageMerge()
            page_merger.add(src, viewrect=(0, y_pos, 1, 0.5))
            yield page_merger.render()

    def create_PDF(self):
        logger.debug("Creating PDF: " + self.pdf)
        writer = PdfWriter()
        for page in PdfReader(self.pdf).pages:
            writer.addpages(self.splitpage(page))
        writer.write(self.TEMP + os.sep + "input.pdf")

    def create_images(self):
        logger.debug("Creating images ")
        zoom_x = 2.0  # horizontal zoom
        zomm_y = 2.0  # vertical zoom
        mat = fitz.Matrix(zoom_x, zomm_y)  # zoom factor 2 in each dimension
        doc = fitz.open(self.TEMP + os.sep + "input.pdf")
        for x in doc:
            pix = x.get_pixmap(alpha=False, matrix=mat)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_name = "{}{}.jpg".format(self.TEMP + os.sep, f"{x.number:4d}")
            img.save(img_name)
        logger.debug("Created images of: ")

    def rename_files(self):
        logger.debug("Renaming files")
        regex = r"[0-9]+\.jpg"
        filelist = glob.glob("Temp" + os.sep + "*.jpg")
        for filename in filelist:
            x = re.search(regex, filename)
            os.rename(str(filename), "Temp" + os.sep + x.group())

    def remove_temp(self):
        if os.path.exists(self.TEMP):
            try:
                shutil.rmtree(self.TEMP)
            except OSError as e:
                logger.error(f"Error: {self.TEMP} : {e.strerror}")

    def convert(self):
        if not os.path.exists(self.TEMP):
            os.makedirs(self.TEMP)
        logger.debug("Starting converting")
        self.create_PDF()
        self.create_images()
        logger.debug("Converted file")
