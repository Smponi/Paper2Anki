import os
import random

import genanki


def create_apkg(name):
    MODELID = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        MODELID,
        "Example",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )
    deckId = random.randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(deckId, name)
    DIRECTORY = "Temp"
    count = 0
    filelist = sorted(os.listdir(DIRECTORY))
    filelist.remove("input.pdf")
    while count < len(filelist):
        field1 = '<img src="%s"\\>' % (filelist[count])
        field2 = '<img src="%s"\\>' % (filelist[count + 1])
        my_note = genanki.Note(model=my_model, fields=[field1, field2])
        my_deck.add_note(my_note)
        count = count + 2
    my_package = genanki.Package(my_deck)
    for x in filelist:
        my_package.media_files.append("Temp" + os.sep + x)
    anki_deck_name = "%s.apkg" % name
    my_package.write_to_file(anki_deck_name)
    print(anki_deck_name)
    return anki_deck_name
