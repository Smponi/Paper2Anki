import os
import shutil
import unittest
from os import listdir
from os.path import isfile, join

import paper2anki


class MyTestCase(unittest.TestCase):
    def test_generation_pdf(self):
        pdf = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "goodNotesLernKarte.pdf"
        )
        paper2anki.createPDF(pdf)
        print(pdf)
        files = [f for f in listdir("Temp") if isfile(join("Temp", f))]
        self.assertEqual(len(files), 1)

    def tearDown(self) -> None:
        try:
            shutil.rmtree("Temp")
        except:
            pass


if __name__ == "__main__":
    unittest.main()
