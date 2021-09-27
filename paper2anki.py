import sys
from Converter import Converter
from AnkiCreator import create_apkg

if __name__ == "__main__":
    pdf = sys.argv[1]
    name = sys.argv[2]
    converter = Converter(pdf, name)
    converter.convert()
    create_apkg(name)
    converter.remove_temp()
