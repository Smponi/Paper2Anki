import sys

from loguru import logger

from Paper2Anki import AnkiCreator
from Paper2Anki.Converter import Converter

if __name__ == "__main__":
    pdf = sys.argv[1]
    name = sys.argv[2]
    logger.debug(f"Converting {pdf} to {name}")
    converter = Converter(pdf, name)
    converter.convert()
    AnkiCreator.create_apkg(name)
    converter.remove_temp()
