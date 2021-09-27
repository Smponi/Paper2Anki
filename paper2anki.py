import sys
from Paper2Anki import AnkiCreator, Converter


if __name__ == "__main__":
    pdf = sys.argv[1]
    name = sys.argv[2]
    converter = Converter.Converter(pdf, name)
    converter.convert()
    AnkiCreator.create_apkg(name)
    converter.remove_temp()
